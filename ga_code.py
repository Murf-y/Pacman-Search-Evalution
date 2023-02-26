# -*- coding: utf-8 -*-
"""GA code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CIEAP63w7YABjU0UbX5Wu3DGOEeZ7NIX

# Fitness function
"""

import os
import numpy as np
from livelossplot.inputs.keras import PlotLossesCallback
from sklearn.metrics import accuracy_score
from scipy import stats
from statistics import mean
import math
import inspect
from tqdm import tqdm
import matplotlib.pyplot as plt

"""# Heuristics"""

# manhattan distance
def manhattan_distance(current, problem):
    goal = problem.goal
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

# eucledian distance
def euclidean_distance(current, problem):
    goal = problem.goal
    return math.sqrt((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2)

#maximum heuristics "minimax"
# def max_heuristic(current, problem):
#     goal = problem.goal
#     return max(abs(current[0] - goal[0]), abs(current[1] - goal[1]))

# #diagonal distance
# def diagonal_distance(current, problem):
#     goal = problem.goal
#     dx = abs(current[0] - goal[0])
#     dy = abs(current[1] - goal[1])
#     return (dx + dy) + (math.sqrt(2) - 2) * min(dx, dy)

# look up pattern database heuristic
"""
# Assume we have a precomputed pattern database called pattern_db

def pattern_database_heuristic(state):
    return pattern_db[state]

"""

# # h^2 heuristic
# def h_squared(current, problem):
#     goal = problem.goal
#     return (current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2

class GeneticAlgorithm:

    def __init__(self, 
                 n_genes,
                 n_iterations,
                 lchrom, 
                 pcross, 
                 pmutation, 
                 crossover_type, 
                 mutation_type, 
                 selection_type, 
                 popsize, 
                 n_elites,
                 problem,
                 random_state = None, algorithm = None):
        

        self.n_genes = n_genes
        self.lchrom = lchrom
        self.popsize = popsize
        self.pcross = pcross
        self.pmutation = pmutation
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type
        self.selection_type = selection_type
        self.random_state = random_state
        self.n_iterations = n_iterations
        self.n_elites = n_elites
        self.problem = problem
        self.algorithm = algorithm
        self.best_fitness_evolution = []
    
        pop = []
        while (len(pop) <= self.popsize):
            chromosome = np.random.randint(2, size= self.n_genes)
            pop.append(chromosome)

            
        # Convert pop to list of solutions
        self.population = [tuple(x) for x in pop]

    def fitness_func(self, solution):
            set_of_h = self.get_heuristic_set_from_ind(individual=solution)
            
            new_heuristic = self.get_new_function_from_set_of_h(set_of_h)
            
            cost = len(self.algorithm(self.problem, heuristic=new_heuristic))
            if cost == 0:
                return 1
            else:
                return 1/cost
    
    def get_fitness_scores(self):
        scores = [self.fitness_func(ind) for ind in self.population]
        return np.array(scores)

    def __append_best_score(self, scores):
        best_score = np.max(scores)
        self.best_fitness_evolution.append(best_score)
        return 'Ok'
    
    def __ranking_selection(self, scores):
        ind = np.argsort(scores)

        s = sum(ind)
        t = np.random.rand() * s
        partial_sum = 0
        i=0
        while(partial_sum <t and i <len(scores)):
            partial_sum += scores[i]

        selected = i
        return selected 
    
    def __roulette_selection(self, scores):
        s = sum(scores)
        t = np.random.rand() * s
        partial_sum = 0
        i=0
        while(partial_sum <t and i <len(scores)):
            partial_sum += scores[i]

        selected = i
        return selected

    def select(self, scores, selection_type):

        if selection_type not in ['ranking', 'roulette']:
            raise ValueError('Type should be ranking or tournament')

        if selection_type == 'ranking':
            ind = self.__ranking_selection(scores)
        elif selection_type == 'roulette':
            ind = self.__roulette_selection(scores)
        else:
            pass
        return ind

    def flip(self, p):
        return 1 if np.random.rand() < p else 0

    def __crossover(self, 
                    parent1, 
                    parent2, 
                    crossover_type,
                    pcross, 
                    pmutation, 
                    mutation_type, 
                    lchrom):
        
        if crossover_type not in ['uniform', 'one_point', 'two_point']:
                raise ValueError('crossover_type should be one of uniform, one_point or multi_point')
            
        if crossover_type == 'one_point':
            index = np.random.choice(range(1, lchrom)) 

            parent1 = list(parent1)
            parent2 = list(parent2)

            child1 = parent1[:index] + parent2[index:]
            child2 = parent2[:index] + parent1[index:]

            if self.flip(pmutation):
                child1 = self.__mutation(child1, mutation_type, pmutation)

            if self.flip(pmutation):
                child2 = self.__mutation(child2, mutation_type, pmutation)

            children = [tuple(child1), tuple(child2)]
        elif crossover_type == 'two_point':
            point1 = np.random.choice(range(1, lchrom)) 
            point2 = np.random.choice(point1, range(lchrom))
            child1 = self.__mutation(parent1[:point1] + parent2[point1: point2] + parent1[point2:],  mutation_type, pmutation, nmutation)
            child2 = self.__mutation(parent2[:point1] + parent1[point1: point2] + parent2[point2:], mutation_type, pmutation, nmutation)
            children = [child1, child2]
        elif crossover_type == 'uniform':
           
            t = np.random.rand()
            temp = np.random.rand(lchrom)
            child1 = self.__mutation([parent1[i] if temp[i] > t else parent2[i] for i in range(len(temp)) ], mutation_type, pmutation, nmutation)
            child2 = self.__mutation([parent2[i] if temp[i] > t else parent1[i] for i in range(len(temp)) ], mutation_type, pmutation, nmutation)
            children = [child1, child2]
               
    
        else:
            child1 = self.__mutation(parent1, mutation_type, pmutation, nmutation)
            child2 = self.__mutation(parent2, mutation_type, pmutation, nmutation)
            children = [child1, child2]
        return children
    
    def get_heuristic_set_from_ind(self, individual):
        set_of_h = []
        for _ in range(len(individual)):
                if individual[_]:
                    if _ == 0:
                        set_of_h.append(manhattan_distance)
                    if _ == 1:
                        set_of_h.append(euclidean_distance)
                    # if _ == 2:
                    #     set_of_h.append(max_heuristic)
                    # if _ == 3:
                    #     set_of_h.append(diagonal_distance)
                    # if _ == 4:
                    #     set_of_h.append(h_squared)
        return set_of_h
    
    def get_new_function_from_set_of_h(self, set_of_h):
        def new_heuristic(state, problem):
            avg = 0
            for h in set_of_h:
              avg += h(state, problem)
            
            if len(set_of_h) == 0:
              return 0
            return avg/len(set_of_h)
        return new_heuristic

    def __mutation(self, individual, mutation_type, pmutation):

        if mutation_type not in ['bitstring', 'inversion', 'swap']:
            raise ValueError('mutation_type should be one of bitstring or inversion or swap')


        index = np.random.choice(len(individual))
        index2 = np.random.choice(len(individual))
        
        # Convert individual to list so that can be modified
        individual_mod = list(individual)
        if mutation_type == 'bitstring':
            individual_mod[index] = 1 - individual_mod[index]
        elif mutation_type == 'inversion':
            individual_mod= individual_mod[0:index] + individual_mod[index2:index-1:-1] + individual_mod[index2+1:]
        elif mutation_type == 'swap':
            individual_mod[index], individual_mod[index2] = individual_mod[index2], individual_mod[index]
        else:
            pass
        
        individual = tuple(individual_mod)

        return individual

    def optimize(self):

        for i in tqdm(range(self.n_iterations)):
            print("iteration number: ", i)

            # calculate fitness score
            scores = self.get_fitness_scores()
            

            # choose the elites of the current population
            ind = np.argsort(scores)

            elites = [self.population[i] for i in ind[-self.n_elites:]]

            #append the elites to the population
            new_population = [tuple(elite) for elite in elites]

            # make selection
            j = self.n_elites
            while j <= self.popsize:
                # select parents from population
                mate1 = self.select(scores, self.selection_type)
                mate2 = self.select(scores, self.selection_type)

                mate1 = tuple(self.population[mate1])
                mate2 = tuple(self.population[mate2])

                if self.flip(self.pcross):
                    children = self.__crossover(mate1, mate2, self.crossover_type, self.pcross, self.pmutation, self.mutation_type, self.lchrom)
                    children = [tuple(child) for child in children]
                    x= False
                else:
                    children = [mate1, mate2]
                    x=True
                
                new_population.append(tuple(children[0]))
                new_population.append(tuple(children[1]))        
                j+=2

            self.population = new_population

        # when n_iterations are over, fitness scores
        scores = self.get_fitness_scores()

        # append best score
        _ = self.__append_best_score(scores)

        # get the result wher he results is the best
        best_score_ind =np.argpartition(scores, 0)[0]
    
        best_solution = self.population[best_score_ind]

        return (best_solution, self.best_fitness_evolution[-1])


    # run the genetic algorithm
    def view_fitness_evolution(self):
        plt.plot(
            range(len(self.best_fitness_evolution)),
            self.best_fitness_evolution
        )




def run_ga(given_problem, algorithm):
    ga = GeneticAlgorithm(
    n_genes = 5,
    n_iterations = 32,
    lchrom = 2, 
    pcross = 0.8, 
    pmutation = 0.05, 
    crossover_type = 'one_point', 
    mutation_type = 'bitstring', 
    selection_type = 'ranking', 
    popsize = 6, 
    n_elites = 2,
    problem = given_problem,
    random_state = 123,
    algorithm= algorithm
    )
    best_solution, best_fitness = ga.optimize()
    ga.view_fitness_evolution()

    best_heuristic = ga.get_new_function_from_set_of_h(ga.get_heuristic_set_from_ind(best_solution))

    return best_heuristic
    