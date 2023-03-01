import math

def manhattan_distance(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

def euclidean_distance(current, goal):
    return math.sqrt((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2)

def max_heuristic(current, goal):
    return max(abs(current[0] - goal[0]), abs(current[1] - goal[1]))

def min_heuristic(current, goal):
    return min(abs(current[0] - goal[0]), abs(current[1] - goal[1]))

def diagonal_distance(current, goal):
    dx = abs(current[0] - goal[0])
    dy = abs(current[1] - goal[1])
    return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)

def euclidean_squared(current, goal):
    return (current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2

def null_heuristic(current, goal):
    return 0

def mean_heuristic(current, goal):
    return (abs(current[0] - goal[0]) + abs(current[1] - goal[1]))/2
