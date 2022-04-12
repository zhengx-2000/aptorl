"""
The training process of Q learning
"""

import numpy as np
import pandas as pd
from ProgOptEnv_Ubuntu import ProgOptEnv
from QL_brain import QLearningTable

if __name__ == "__main__":
    env = ProgOptEnv()
    RL = QLearningTable(actions=list(range(env.n_actions)))
    max_episode = 200
    max_episode_length = 100
    steps_count = pd.DataFrame(index=np.arange(0, max_episode), columns=('steps', 'win'))

    for episode in range(max_episode):
        print('\n episode:%d' % episode)
        # initialization
        observation = env.reset()
        episode_count = 0
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
            # print('observation_', observation_)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, info, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                if info == 'win':
                    win = 1
                else:
                    win = 0
                break
        steps_count.loc[episode] = [episode_count, win]

    # end of game
    print('game over')
    RL.q_table.to_excel('QL_qtable_result.xlsx')
    steps_count.to_excel('QL_step_count.xlsx')
    env.destroy()
