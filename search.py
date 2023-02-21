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

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"


    class DFSSearchProblemNode:
        """
        A node in the search tree. Contains a pointer to the parent
        (the node that this is a successor of) and to the actual
        state for this node. Note that if a state is arrived at by
        two paths, then there are two nodes with the same state.  Also
        includes the action that got us to this state.
        

        No need to include the cost in this node implementation, as we are using DFS
        """
        def __init__(self, state, parent, action):
            self.state = state
            self.parent = parent
            self.action = action
        
        def get_path(self):
            """
            Returns a list of actions that got us to this node
            """
            path = []
            node = self
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path
        
        def __eq__(self, other):
            return self.state == other.state
        
        def __hash__(self):
            return hash(self.state)
        
        def __str__(self):
            return str(self.state)
    
    # Initialize the frontier with the start state
    frontier = util.Stack()
    frontier.push(DFSSearchProblemNode(problem.getStartState(), None, None))

    # Initialize the explored set to be empty
    explored = set()

    # Loop until the frontier is empty
    while not frontier.isEmpty():
        # Remove a node from the frontier
        node = frontier.pop()
        # If the node contains a goal state then return the corresponding solution
        if problem.isGoalState(node.state):
            return node.get_path()

        if node.state not in explored:
            # Add the node to the explored set
            explored.add(node.state)
            # Expand the node, adding the resulting nodes to the frontier
            for child_state, action_to_child, cost_of_action  in problem.getSuccessors(node.state):
                frontier.push(DFSSearchProblemNode(child_state, node, action_to_child))
    
    # If the frontier is empty then return failure
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    class BFSSearchProblemNode:
        """
        A node in the search tree. Contains a pointer to the parent
        (the node that this is a successor of) and to the actual
        state for this node. Note that if a state is arrived at by
        two paths, then there are two nodes with the same state.  Also
        includes the action that got us to this state.
        

        No need to include the cost in this node implementation, as we are using BFS
        """
        def __init__(self, state, parent, action):
            self.state = state
            self.parent = parent
            self.action = action
        
        def get_path(self):
            """
            Returns a list of actions that got us to this node
            """
            path = []
            node = self
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path
        
        def __eq__(self, other):
            return self.state == other.state
        
        def __hash__(self):
            return hash(self.state)
        
        def __str__(self):
            return str(self.state)
    
    # Initialize the frontier with the start state
    frontier = util.Queue()

    frontier.push(BFSSearchProblemNode(problem.getStartState(), None, None))

    # Initialize the explored set to be empty
    explored = set()

    # Loop until the frontier is empty
    while not frontier.isEmpty():
        # Remove a node from the frontier
        node = frontier.pop()
        # If the node contains a goal state then return the corresponding solution
        if problem.isGoalState(node.state):
            return node.get_path()

        if node.state not in explored:
            # Add the node to the explored set
            explored.add(node.state)
            # Expand the node, adding the resulting nodes to the frontier
            for child_state, action_to_child, cost_of_action  in problem.getSuccessors(node.state):
                frontier.push(BFSSearchProblemNode(child_state, node, action_to_child))
    
    # If the frontier is empty then return failure
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    class UCSNode:
        """
        A node in the search tree. Contains a pointer to the parent
        (the node that this is a successor of) and to the actual
        state for this node. Note that if a state is arrived at by
        two paths, then there are two nodes with the same state.  Also
        includes the action that got us to this state.
        """
        def __init__(self, state, parent, action, cost):
            self.state = state
            self.parent = parent
            self.action = action
            self.cost = cost
        
        def get_path(self):
            """
            Returns a list of actions that got us to this node
            """
            path = []
            node = self
            while node.parent:
                path.append(node.action)
                node = node.parent
            path.reverse()
            return path
        
        def __eq__(self, other):
            return self.state == other.state
        
        def __hash__(self):
            return hash(self.state)
        
        def __str__(self):
            return str(self.state)

    # Initialize the frontier with the start state
    frontier = util.PriorityQueueWithFunction(lambda node: node.cost)
    frontier.push(UCSNode(problem.getStartState(), None, None, 0))

    # Initialize the explored set to be empty
    explored = set()

    # Loop until the frontier is empty
    while not frontier.isEmpty():
        # Remove a node from the frontier
        node = frontier.pop()
        # If the node contains a goal state then return the corresponding solution
        if problem.isGoalState(node.state):
            return node.get_path()

        if node.state not in explored:
            # Add the node to the explored set
            explored.add(node.state)
            # Expand the node, adding the resulting nodes to the frontier
            for child_state, action_to_child, cost_of_action  in problem.getSuccessors(node.state):
                frontier.push(UCSNode(child_state, node, action_to_child, node.cost + cost_of_action))
    # If the frontier is empty then return failure
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
