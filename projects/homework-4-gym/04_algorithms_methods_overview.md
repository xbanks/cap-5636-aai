Overview of Methods used in Class
=================================

## Search Algorithms

__BFS__:

This is a breadth first search algorithm. It is used when an optimal solution (in terms of path length) is needed to be found. It searches each node in each depth of the three before moving on to the next depth.

__DFS__:

This is a depth first search. It's used when a solution should be found quickly. It searches as far down a specific path as possible, and if it doesn't find a solution, it traverses all the way down the next path.

__UCS__:

Uniform cost search is a search that expands nodes based on an observed cost. It takes path cost into account and produces an optimal solution in a more reasonable amount of time.

__Greedy Search__:

Greedy search is a heuristic based informed search algorithm. It moves directly towards the goal based on a given distance heuristic. This is useful when you want the most straightforward solution towards the goal, execpt for the fact that the heuristic might be very wrong, and can therefore lead you down a bad path.

__A Star__:

A\* Search is an informed search algorithm, which uses a combination of uniform cost search and greedy search. It expands nodes based on the backwards and forward costs. This produces a search that generally searches in the direction of the goal.

## Adversarial Searches

__MinMax__:

Minmax is a search algorithm that takes into account a given opponent. It chooses a move based on it's perception of what the opponent will do in their optimal case. This produces an agent that always tries to act as if it's playing against a perfect agent.

__Alpha-Beta Pruning__:

Alpha beta pruning solves the problem of computing values for unnecessary subtrees in a search tree. It essentially checks the min/max values of certain nodes, and if they are greater/less than the already explored nodes then it can choose to prune the parts of the tree which are now deemed unnecessary to traverse.

__ExpectiMax__:

Expectimax is a search algorithm that takes into account the fact that agents are not perfect, and will not always take the most optimal move. So it calculates the expected utilities of certain moves based on the values that are possible, along with a given chance probability of the opponent taking a certain move.

## Markov Decision Processes


MDPs provide a probabalistic model of an environment given states and actions. These model the world in such a way that the next state is based on the current one, and the objective is to compute an optimal policy which maps from states in the MDP to the optimal actions that should be taken at each of those states. This is considered __offline learning__.

__Value Iteration__:

Value iteration is a method for finding the steady state values for states in an MDP by iteratively computing the values for K timesteps until convergance. 

__Policy Iteration__:

Policy iteration is a method for coming up with an optimal policy. It's done by using value iteration and policy evaluation to compute the values for a random policy, using policy extraction to find a newer more optimal policy using those fixed values.

## Reinforcement Learning

Reinforcement learning is very similar to MDPs, except that we no longer know the transition function, nor the reward function, so we must use experiences to _learn_ these. This is considered __online learning__.

__Q Value Iteration and Q-Learning__:

Q-Values are the values that each action provides you at a given state. Q-Learning is the process of approximating these values using experiences. This solves the problem of finding optimal actions in an online learning algorithm, since we can update our previous estimations of the value of an action given our new experience.

__Exploration and Exploitation__:

This is the problem of choosing to go with the learned and currently best policy (exploitation), or choosing to explore the action space randomly in order to get a more varied learning experience. This solves the problem of prematurely sticking to a decent policy, when a better policy can be found with a little exploration.

__Feature Based Learning__:

Sometimes the state space is huge, so it's useful to sum up this information into a smaller set of representative features. Using this smaller set of rich features can make learning easier, as well as faster and more space efficient.

__Approximate Q-Learning__:

This is similar to regular Q-Learning except it approximates a linear function based on the smaller feature set used. Often we use regularization techniques to ensure that the coefficients for the features don't skew too far out.

__Deep Q Learning/Cross Entropy method__:

Deep Q Learning uses neural networks to approximate the Q-Value function required to choose actions in the transition function. It allows you to use a set of features as the input, and it can be trained to approximate the Q-Values of a given state. You can then use a cross entropy loss to compute the difference in action choice to what the correct one should have been in order to update the weights on the different layers.