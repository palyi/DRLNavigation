# DRLNavigation
Navigating by Deep Reinforcement Learning

Quick Summary:

The task solved by the contents of this repository is navigating in a finite space featuring colored objects (bananas). The agent of this reinforcement learning scenario is trained to collect as many of the target objects as possible.

Apart from the above introduction, this repository contains the code that used for training the agent, along with the trained model weights. Additionally, I attached a report describing my learning algorithm.

Usage (inlc. pre-requisites):

1. Install Anaconda with TensorFlow 1.7.1
2. Install Cython by pip3 install cython
3. Install pyTorch by pip3 install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
  This command lets you install pyTorch via Pip, in a Windows environment, utilizing CUDA 10.1 (commands for other environments can be generated at pyTorch.org
4. Install Unity Machine Learning Agents by pip3 install mlagents



----

Detailed Description:

The project is written in pyTorch and Python3. The functional, documented code is included in this repository, alongside with the model weights of the successful agent.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. The action space consists of four discrete actions, as follows:
0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

Training the agent:

Running the code:

----

Report:

Learning algorithm:
Plot of rewards:
Ideas for future work:

