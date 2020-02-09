<h1>Report:</h1>

<h2>Learning algorithm</h2>

The software is implementing Deep Reinforcement Learning. The agent makes use of two artificial neural networks to build and represent action-values as weights in the primary Q network and the target Q network as well.

1. The solution initializes an empty replay memory as first,
2. then initializes action value primary and target networks both,
3. finally, episode-by-episode, it takes input frames stacked

<h2>Model architecture of the deep Q neural network applied</h2>

The artificial neural network applied (same structure for both) is initialized with the following structure:<br>
self.fc1 = nn.Linear(state_size, fc1_units)<br>
self.fc2 = nn.Linear(fc1_units, fc2_units)<br>
self.fc3 = nn.Linear(fc2_units, action_size)<br>
<br>
while the forward propagation is implemented as:<br>
x = F.relu(self.fc1(state))<br>
x = F.relu(self.fc2(x))<br>
return self.fc3(x)<br>

<h2>Hyperparameters chosen</h2>

Similarly to the example task (lunar lander), I applied the following hyperparameters: <br>
BUFFER_SIZE = int(1e5)  # replay buffer size <br>
BATCH_SIZE = 64         # minibatch size <br>
GAMMA = 0.99            # discount factor <br>
TAU = 1e-3              # for soft update of target parameters <br>
LR = 5e-4               # learning rate <br>
UPDATE_EVERY = 4        # how often to update the network <br>

<h2>Plot of rewards per episode</h2> 

The agent is able to receive an average reward (over 100 episodes) of at least +13. <br>
![Result chart](chart2.JPG)
<br>
Number of episodes needed to solve the environment.
![Result log](terminal2.JPG)

<h2>Running the agent with the best weights achieved:</h2>
<br>
![Test Result chart](RunChart.JPG)
<br>
Number of episodes needed to solve the environment.
![Test Result log](runTerminal.JPG)

<h2>Ideas for future work</h2>
I would most probably go for Prioritized Experience Replay to further improve the performance of the algorithm. By that approach, the agent could learn more of certain scenarios that are proven as more important, hence visiting those more frequently.
