# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node(object):
    """
    A simple node class that represents a given node in a search tree, holding both the current state,
    and the path taken to get to the current state.
    """
    def __init__(self, state, path = []):
        self.state = state
        self.path = path

def simpleSearch(problem, queuingFunction):
    """
    This search function performs the generic search algorithm. 
    The main customization point is in the queue and it's associated priority function.

    This can be used by most of the later search algorithms simply by passing in a different queue.
    """
    start_state = problem.getStartState()

    node = Node(start_state)
    visited_nodes = set([start_state])

    queue = util.PriorityQueueWithFunction(queuingFunction)
    while not problem.isGoalState(node.state):
        successors = problem.getSuccessors(node.state)

        for state, direction, cost in successors:
            if state not in visited_nodes:
                newpath = node.path + [direction]
                n = Node(state, newpath)
                queue.push(n)

        node = queue.pop()
        while node.state in visited_nodes:
            node = queue.pop()
        visited_nodes.add(node.state)

    return node.path

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    """
    This runs the simple search with a FIFO Stack
    """
    queuingFunction = lambda node: - len(node.path)
    return simpleSearch(problem, queuingFunction)

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
    This runs the simple search with a LIFO Queue
    """
    queuingFunction = lambda node: len(node.path)
    return simpleSearch(problem, queuingFunction)

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    queuingFunction = lambda node: problem.getCostOfActions(node.path)
    return simpleSearch(problem, queuingFunction)

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    queuingFunction = lambda node: problem.getCostOfActions(node.path) + heuristic(node.state, problem)
    return simpleSearch(problem, queuingFunction)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
