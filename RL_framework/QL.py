"""
Q-Learning environment for programme optimisation
Author: Xiao Zheng
Date: 23/3/2022
"""
import numpy as np
from ProgOptEnv_Windows import ProgOptEnv

env = ProgOptEnv()
# reset
# action_space
# render
# step

max_number_of_steps = 100
goal_average_scores = 0.2
num_consecutive_iterations = 100
num_episodes = 2
last_time_scores = np.zeros(num_consecutive_iterations)  # 只存储最近100场的得分（可以理解为是一个容量为100的栈）

q_table = np.random.uniform(low=0, high=1, size=(100 * 5, 2))


# 分箱处理函数，把[clip_min,clip_max]区间平均分为num段，位于i段区间的特征值x会被离散化为i
def bins(clip_min, clip_max, num):
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]


# 离散化处理，将由2个连续特征值组成的状态矢量转换为一个0~~255的整数离散值
def digitize_state(observation):
    # 将矢量打散回2个连续特征值
    line_pos, runtime = observation

    # 分别对各个连续特征值进行离散化（分箱处理）
    digitized = [np.digitize(line_pos, bins=bins(0, 100, 100)),  # 0->0, 1->1, 2->2, ..., 99->99
                 np.digitize(runtime, bins=bins(0, 1.5, 5))]  # (-inf,0.3)->0, [0.3,0.6)->1, [0.6,0.9)->2, [0.9,
    # 1.2)->3, [1.2,1.5)->3, [1.5,+inf)->5

    print('Digitized:')
    print(digitized)
    # 将2个离散值再组合为一个离散值，作为最终结果
    return sum([x * (2 ** i) for i, x in enumerate(digitized)])


# 根据本次的行动及其反馈（下一个时间步的状态），返回下一次的最佳行动
def get_action(state, action, observation, reward):
    next_state = digitize_state(observation)  # Get the state in the observation
    next_action = np.argmax(q_table[next_state])  # Simple greedy strategy
    # -------------------------------------训练学习，更新q_table----------------------------------
    alpha = 0.2  # 学习系数α
    gamma = 0.99  # 报酬衰减系数γ
    q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (
            reward + gamma * q_table[next_state, next_action])
    # -------------------------------------------------------------------------------------------
    return next_action, next_state


if __name__ == "__main__":
    # 重复进行一场场的游戏
    for episode in range(num_episodes):
        observation = env.reset()  # 初始化本场游戏的环境
        state = digitize_state(observation)  # 获取初始状态值
        action = np.argmax(q_table[state])  # 根据状态值作出行动决策
        episode_reward = 0
        # 一场游戏分为一个个时间步
        for step in range(max_number_of_steps):
            # env.render()    # 更新并渲染游戏画面
            observation, reward, done, info = env.step(action)  # 获取本次行动的反馈结果
            action, state = get_action(state, action, observation, reward)  # 作出下一次行动的决策
            episode_reward += reward
            print('Observation: ')
            print(observation)
            print('Info: ')
            print(info)
            if done:
                print('%d Episode finished after %f steps / mean %f' % (episode, step + 1, last_time_scores.mean()))
                last_time_scores = np.hstack((last_time_scores[1:], [episode_reward]))  # 更新最近100场游戏的得分stack
                break
            if last_time_scores.mean() >= goal_average_scores:
                print('Episode %d train agent successfully!' % episode)
                break
    print('Failed!')
