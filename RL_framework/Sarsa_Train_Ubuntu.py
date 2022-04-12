"""
The training process of Sarsa
"""

import numpy as np
import pandas as pd
from ProgOptEnv_Ubuntu import ProgOptEnv
from Sarsa_brain import SarsaTable

if __name__ == "__main__":
    env = ProgOptEnv()
    RL = SarsaTable(actions=list(range(env.n_actions)))
    max_episode = 200
    max_episode_length = 100
    steps_count = pd.DataFrame(index=np.arange(0, max_episode), columns=('steps', 'total_reward'))

    for episode in range(max_episode):
        print('\n episode:%d' % episode)
        # initialization
        observation = env.reset()
        episode_count = 0
        reward_total = 0
        win = 0

        # RL choose action based on observation
        action = RL.choose_action(str(observation))

        for episode_length in range(max_episode_length):
            episode_count += 1

            # fresh env
            # env.render()

            # RL take action and get next observation and reward
            observation_, reward, done, info = env.step(action)
            reward_total += reward
            # print('observation_', observation_)

            # RL choose action based on next observation
            action_ = RL.choose_action(str(observation_))
            # print('action:', action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, info, str(observation_), action_)

            # swap observation and action
            observation = observation_
            action = action_

            # break while loop when end of this episode
            if done:
                break
        steps_count.loc[episode] = [episode_count, reward_total]

    # end of game
    print('game over')
    RL.q_table.to_excel('Sarsa_qtable_result.xlsx')
    steps_count.to_excel('Sarsa_step_and_reward_count.xlsx')
    env.destroy()
