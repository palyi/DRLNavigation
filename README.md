# DRLNavigation
<h1>Navigating by Deep Reinforcement Learning (Deep Q Learning)</h1>

<h2>Quick Summary:</h2>

The task solved by the contents of this repository is navigating in a finite space featuring colored objects (bananas). The agent of this reinforcement learning scenario is trained to collect as many of the target objects as possible.

Apart from the above introduction, this repository contains the code that used for training the agent, along with the trained model weights. Additionally, I attached a report describing my learning algorithm, and one program dedicated to running the agent with the weights saved as a result of the last training.

<h2>Usage:</h2>

<h3>Installing dependencies</h3>

1. Install Anaconda and create an environment
2. Install pyTorch by pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
  This command lets you install pyTorch via Pip, in a Windows environment, utilizing CUDA 10.1 (commands for other environments can be generated at pyTorch.org
3. Install Unity Machine Learning Agents by pip install mlagents
4. The environment is provided by a Windows (64-bit) executable, which can be downloaded from: https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip

<h3>Downloading files needed</h3>

Clone this git repository in your directory of choice.

------------

<h2>Detailed Description:</h2>

The project is written in pyTorch and Python3. The functional, documented code is included in this repository, alongside with the model weights of the successful agent, contained in the file named checkpoint.pth.

<h3>Characteristics of the solution:</h3> 

<b><u>State space:</u></b><br>
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. 

<b><u>Action space:</u></b><br>
The action space consists of four discrete actions, as follows:
0 - move forward.
1 - move backward.
2 - turn left.
3 - turn right.

<b><u>Rewards:</u></b><br>
A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The task is episodic and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes. (The uploaded trainer was given the aim of a score of 16.5.)

--------------

<h2>Training the agent:</h2>
In order to train the agent, simply run Navigation.py (it contains a variable that is set to true, named train_mode).

<h2>Running the trained agent:</h2>

To run the software with the latest weights saved, type python TestTrainedAgent.py at the Anaconda command prompt, with the above described Anaconda environment being active.
