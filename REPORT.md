<h1>Report:</h1>

<h2>Learning algorithm</h2>

The software is implementing Deep Reinforcement Learning. The agent makes use of two artificial neural networks to build and represent action-values as weights in the primary Q network and the target Q network as well.

1. The solution initializes an empty replay memory as first,
2. then initializes action value primary and target networks both,
3. finally, episode-by-episode, it takes input frames stacked

<h2>Model architecture of the deep Q neural network applied</h2>

<h2>Hyperparameters chosen</h2>
History of past data is buffered in a replay pool 

<h2>Plot of rewards per episode</h2> 

The agent is able to receive an average reward (over 100 episodes) of at least +13. 
![Result chart](chart1.JPG)

Number of episodes needed to solve the environment.
![Result log](terminal.JPG)


Ideas for future work:
I would most probably go for Prioritized Experience Replay to further improve the performance of the algorithm. By that approach, the agent could learn more of certain scenarios that are proven as more important, hence visiting those more frequently.
