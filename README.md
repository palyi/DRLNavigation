# DRLNavigation
<h1>Navigating by Deep Reinforcement Learning (Deep Q Learning)</h1>

<h2>Quick Summary:</h2>

The task solved by the contents of this repository is navigating in a finite space featuring colored objects (bananas). The agent of this reinforcement learning scenario is trained to collect as many of the target objects as possible.

Apart from the above introduction, this repository contains the code that used for training the agent, along with the trained model weights. Additionally, I attached a report describing my learning algorithm.

<h2>Usage:</h2>

<h3>Installing dependencies</h3>

1. Install Anaconda and create an environment with TensorFlow 1.7.1
2. Install Cython by pip install cython
3. Install pyTorch by pip install torch===1.4.0 torchvision===0.5.0 -f https://download.pytorch.org/whl/torch_stable.html
  This command lets you install pyTorch via Pip, in a Windows environment, utilizing CUDA 10.1 (commands for other environments can be generated at pyTorch.org
4. Install Unity Machine Learning Agents by pip3 install mlagents

<h3>Downloading files needed</h3>

1. Clone this git repository in your directory of choice.

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

The task is episodic and in order to solve the environment, the agent must get an average score of +13 over 100 consecutive episodes.

--------------

<h2>Training the agent:</h2>
In order to train the agent, the boolean variable in the DQN function of Navigation.py should be set true by train_mode=True, meaning so that resetting the environment should be adjusted as follows:

env_info = env.reset(train_mode=True)[brain_name]

<h2>Running the code:</h2>

To run the software, type python Navigation.py at the Anaconda command prompt, with the above described Anaconda environment being active.

----

<h2>Report:</h2>

![Result chart](chart1.JPG)
then
![Result log](terminal.JPG)

Learning algorithm:
Plot of rewards:
Ideas for future work:

