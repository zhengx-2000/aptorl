"""
The training process of Q learning
"""

import numpy as np
import pandas as pd
from ProgOptEnv_Windows import ProgOptEnv
from QL_brain import QLearningTable

if __name__ == "__main__":
    env = ProgOptEnv()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    max_episode = 200
    max_episode_length = 100
    stat_episode = pd.DataFrame(index=np.arange(0, max_episode), columns=('steps', 'total_reward'))

    for episode in range(max_episode):
        print('\n episode:%d' % episode)
        # initialization
        observation = env.reset()
        episode_count = 0
        reward_total = 0
        win = 0
        for episode_length in range(max_episode_length):
            episode_count += 1

            # fresh env
            # env.render()

            # RL choose action based on observation
            action = RL.choose_action(str(observation))
            # print('action:', action)

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
        stat_episode.loc[episode] = [episode_count, reward_total]

    # end of game
    print('game over')
    RL.q_table.to_excel('QL_qtable_result.xlsx')
    stat_episode.to_excel('QL_step_and_reward_episode.xlsx')
    env.destroy()
