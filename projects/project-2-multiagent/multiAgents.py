# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        from random import random

        pos = currentGameState.getPacmanPosition()
        food = currentGameState.getFood()
        ghostStates = currentGameState.getGhostStates()
        scaredTimes = [ghostState.scaredTimer for ghostState in ghostStates]

        distance = lambda x: util.manhattanDistance(x, newPos)
        ghostPositions = map(lambda x: x.getPosition(), newGhostStates)
        distance_to_ghosts = sum(map(distance, ghostPositions))

        def food_distance(foodList):
            distance_to_closest_food = float('inf')
            for pellet in foodList:
                distance_to_closest_food = min(distance_to_closest_food, distance(pellet))
            return distance_to_closest_food

        distance_to_food = food_distance(food.asList())
        distance_to_new_food = food_distance(newFood.asList())

        better_score = successorGameState.getScore() > currentGameState.getScore()
        lost = successorGameState.isLose()
        won = successorGameState.isWin()
        less_food = len(newFood.asList()) < len(food.asList())
        closer_to_food = distance_to_new_food < distance_to_food
        ghosts_too_close = distance_to_ghosts < 4

        value = (better_score * 5) \
                - (lost * 100) \
                + (won * 100) \
                + (less_food * 5) \
                + (closer_to_food) \
                + random() \
                + (1.0 / (distance_to_food + 0.00000001))

        if ghosts_too_close:
            non_zero_distance = distance_to_ghosts + 0.000001
            ghost_penalty = (1.0 / non_zero_distance) * 100
            value -= ghost_penalty

        return value

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        def max_value(gameState, agentNum, depth):
            max_val = float('-inf')
            max_action = None
            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, a = value(successorGameState, agentNum+1, depth-1)
                if val >= max_val:
                    max_val = val
                    max_action = action
            return max_val, max_action

        def min_value(gameState, agentNum, depth):
            min_val = float('inf')
            min_action = None

            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, a = value(successorGameState, agentNum+1, depth-1)
                if val < min_val:
                    min_val = val
                    min_action = action
            return min_val, min_action

        def value(gameState, agentNum, depth):
            if gameState.isWin() or gameState.isLose():
                return gameState.getScore(), None

            if depth == 0:
                return self.evaluationFunction(gameState), None

            agent = agentNum % gameState.getNumAgents()

            if agent == 0:
                return max_value(gameState, agent, depth)
            else:
                return min_value(gameState, agent, depth)

        iters = self.depth * gameState.getNumAgents()
        val, action = value(gameState, self.index, iters)
        return action

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def max_value(gameState, agentNum, depth, alpha, beta):
            max_val = float('-inf')
            max_action = None
            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, a = value(successorGameState, agentNum+1, depth-1, alpha, beta)
                if val >= max_val:
                    max_val = val
                    max_action = action
                if max_val > beta:
                    return max_val, max_action
                alpha = max(alpha, max_val)
            return max_val, max_action

        def min_value(gameState, agentNum, depth, alpha, beta):
            min_val = float('inf')
            min_action = None

            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, a = value(successorGameState, agentNum+1, depth-1, alpha, beta)
                if val < min_val:
                    min_val = val
                    min_action = action
                if min_val < alpha:
                    return min_val, min_action
                beta = min(beta, min_val)
            return min_val, min_action

        def value(gameState, agentNum, depth, alpha, beta):
            if gameState.isWin() or gameState.isLose():
                return gameState.getScore(), None

            if depth == 0:
                return self.evaluationFunction(gameState), None

            agent = agentNum % gameState.getNumAgents()

            if agent == 0:
                return max_value(gameState, agent, depth, alpha, beta)
            else:
                return min_value(gameState, agent, depth, alpha, beta)

        iters = self.depth * gameState.getNumAgents()
        alpha = float('-inf')
        beta = float('inf')
        val, action = value(gameState, self.index, iters, alpha, beta)
        return action

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def max_value(gameState, agentNum, depth):
            max_val = float('-inf')
            max_action = None
            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, _ = value(successorGameState, agentNum+1, depth-1)
                if val >= max_val:
                    max_val = val
                    max_action = action
            return max_val, max_action

        def expected_value(gameState, agentNum, depth):
            exp_sum = 0
            prob = 1.0 / len(gameState.getLegalActions(agentNum))

            for action in gameState.getLegalActions(agentNum):
                successorGameState = gameState.generateSuccessor(agentNum, action)
                val, _ = value(successorGameState, agentNum+1, depth-1)
                exp_sum += val
            exp_val = exp_sum * prob
            return exp_val, None

        def value(gameState, agentNum, depth):
            if gameState.isWin() or gameState.isLose():
                return gameState.getScore(), None

            if depth == 0:
                return self.evaluationFunction(gameState), None

            agent = agentNum % gameState.getNumAgents()

            if agent == 0:
                return max_value(gameState, agent, depth)
            else:
                return expected_value(gameState, agent, depth)

        iters = self.depth * gameState.getNumAgents()
        val, action = value(gameState, self.index, iters)
        return action

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    from pprint import pprint
    from operator import attrgetter
    from random import random

    # pprint(currentGameState.data.__dict__)
    # pprint(currentGameState.data.agentStates[0].__dict__)
    # pprint(currentGameState.data.agentStates[1].__dict__)
    # pprint(currentGameState.data.agentStates[1].configuration.__dict__)
    pacman = currentGameState.data.agentStates[0]
    ghosts = currentGameState.data.agentStates[1:]
    ghost_scared_timers = map(attrgetter('scaredTimer'), ghosts)
    ghost_positions = map(attrgetter('configuration.pos'), ghosts)

    gs = zip(ghost_scared_timers, ghost_positions)

    moved = currentGameState.data._agentMoved
    food = currentGameState.data.food.asList()
    capsules = currentGameState.data.capsules
    score = currentGameState.data.score
    scoreChange = currentGameState.data.scoreChange
    win = currentGameState.data._win
    lose = currentGameState.data._lose

    dist_func = lambda x: util.manhattanDistance(pacman.configuration.pos, x)
    distance_to_ghosts = sum(map(dist_func, ghost_positions))

    value = score \
            + win * 100 \
            + lose * -1000 \
            + (1.0 / (len(food) + 1)) * 10 \
            + (1.0 / (len(capsules) + 1)) \
            + random() / 10.0
            # + distance_to_ghosts \

    distance_to_closest_food = float('inf')
    for pellet in food:
        distance_to_closest_food = min(distance_to_closest_food, dist_func(pellet))

    if distance_to_closest_food < float('inf'):
        value += 10.0 / distance_to_closest_food

    def min_dist(lst):
        closest_dist = float('inf')
        for point in lst:
            closest_dist = min(closest_dist, dist_func(point))
        return closest_dist

    distance_to_closest_cap = min_dist(capsules)
    if distance_to_closest_cap < float('inf'):
        value += 1.0 / distance_to_closest_cap

    distance_to_ghosts = min_dist(ghost_positions)
    ghosts_too_close = distance_to_ghosts < 4
    if ghosts_too_close:
        non_zero_distance = distance_to_ghosts + 0.000001
        ghost_penalty = (1.0 / non_zero_distance) * 100
        value -= ghost_penalty

    return value

# Abbreviation
better = betterEvaluationFunction

