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

