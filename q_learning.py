import os
import random
import time

import gym
import numpy as np

env = gym.make(
    "FrozenLake-v0"
)  # is_slippery=False, to remove stochastic nature of the env.

action_space_size = env.action_space.n  # total number of unique action available
state_space_size = env.observation_space.n  # total number of state


# Creating the Q table based on the state and action space shape.
q_table = np.zeros((state_space_size, action_space_size))

# Some constants

num_episodes = 10000
max_steps_per_episode = 100
learning_rate = 0.1  # In q learning algo
discount_rate = 0.99  # In q learning algo

exploration_rate = 1  # Initialization of exploration rate
exploration_decay_rate = 0.001  # Rate at which exploration will decay

rewards_all_episodes = []

for episode in range(num_episodes):
    state = env.reset()
    done = False
    reward_current_episode = 0
    for step in range(max_steps_per_episode):

        exploration_rate_threshold = random.uniform(0, 1)

        if exploration_rate_threshold > exploration_rate:  # Performing exploitation
            # Greedy action, choose action (index) with highest Q value for current state
            action = np.argmax(q_table[state, :])
        else:
            action = np.random.randint(0, 4)

        new_state, reward, done, info = env.step(action)  # Executing the action

        # Update the Q table
        q_table[state, action] = q_table[state, action] + learning_rate * (
            reward
            + discount_rate * np.max(q_table[new_state, :])
            - q_table[state, action]
        )

        state = new_state
        reward_current_episode += reward

        if done == True:  # If episode is over start new episode
            break

    exploration_rate = (
        exploration_rate - exploration_rate * exploration_decay_rate
    )  # reducing exploration rate after each episode
    rewards_all_episodes.append(reward_current_episode)  # reward per episode

# print(rewards_all_episodes) # To observe reward achieved in each epsiode as time goes by.


def clear():  # For aesthetics
    os.system("cls")


clear()

for episode in range(1):
    state = env.reset()
    done = False
    print(f"Episode Number: {episode+1}\n")
    time.sleep(1)  # Delay to read

    for step in range(max_steps_per_episode):
        clear()
        env.render()  # Render current state of the env to the display
        time.sleep(1)

        action = np.argmax(q_table[state, :])  # Greedy action from Q table.

        new_state, reward, done, info = env.step(action)

        if done:  # if our current episode terminated
            clear()
            env.render()  # Observe agent where it is when episode terminated
            if reward == 1:  # Episode ended with goal achieved
                print("Agent reached the goal")
                time.sleep(3)
            else:  # The agent fell through a hole
                print("Agent fell through a hole")
                time.sleep(3)
            clear()
            break  # From current episode
        state = new_state

env.close()
