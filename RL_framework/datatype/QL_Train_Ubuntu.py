"""
The training process of Q learning

Author: Morvan Zhou
Author: Xiao Zheng
"""

import numpy as np
import pandas as pd
from ProgOptEnv_Ubuntu import ProgOptEnv
from QL_brain import QLearningTable

if __name__ == "__main__":
    env = ProgOptEnv()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    max_episode = 1000
    max_episode_length = 200
    stat_episode = pd.DataFrame(index=np.arange(0, max_episode), columns=('steps', 'total_reward', 'end_state'))

    for episode in range(max_episode):
        print('\n episode:%d' % episode)
        # initialization
        observation = env.reset()
        episode_count = 0
        reward_total = 0
        for episode_length in range(max_episode_length):
            episode_count += 1

            # fresh env
            # env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done, info = env.step(action)
            reward_total += reward

            # RL learn from this transition
            RL.learn(str(observation), action, reward, info, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
        stat_episode.loc[episode] = [episode_count, reward_total, observation]

    # end of game
    print('game over')
    RL.q_table.to_excel('QL_qtable_result.xlsx')
    stat_episode.to_excel('QL_episode_reward_state.xlsx')
    env.destroy()
