from unityagents import UnityEnvironment
import numpy as np
import random
import torch
from collections import deque
import matplotlib.pyplot as plt
from agent import Agent #reference to the agent.py include file

env = UnityEnvironment(file_name="e:\\Development\\DeepReinf\\DQN2-Bananas\Banana.exe")
brain_name = env.brain_names[0]
brain = env.brains[brain_name]
env_info = env.reset(train_mode=False)[brain_name]
action_size = brain.vector_action_space_size
state = env_info.vector_observations[0]
state_size = len(state)
scores=[]

agent = Agent(state_size=state_size, action_size=action_size, seed=0)
agent.qnetwork_local.load_state_dict(torch.load('e:\\Development\\DeepReinf\\DQN2-Bananas\checkpoint.pth'))
n_episodes=100
for i_episode in range(1, n_episodes+1):
        env_info = env.reset(train_mode=False)[brain_name]
        state = env_info.vector_observations[0]
        score = 0
        while True:
            action = agent.act(state, eps=0).astype(int) #IT DOES NOT WORK WITHOUT TYPE CASTING !!!!
            env_info=env.step(action)[brain_name]
            next_state=env_info.vector_observations[0] 
            reward=env_info.rewards[0]
            done=env_info.local_done[0] 
            score += reward
            state = next_state
            if done:
                scores.append(score)              # save most recent score
                print('\rEpisode {}\tAverage Score: {:.2f}'.format(i_episode, np.mean(scores)), end="")
                break 

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(np.arange(len(scores)), scores)
plt.ylabel('Score')
plt.xlabel('Episode #')
plt.show()
env.close