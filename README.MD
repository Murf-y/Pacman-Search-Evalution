<h1 align="center">Pacman Search
    <img src="./gifs/200w.webp" width="40">
</h1>

<h3 align="center"> CSC460 - Artificial Intelligence ©️</h3>
<h5 align="center"> Project Phase 1 </h5>

<p align="center">
  <img src="./gifs/big.gif" alt="Animated gif pacman game" height="282px" width="500" style="border-radius:2rem">
</p>

<br>
<br>
<h1 id="outline"> Outline 📜</h1>
<ol>
    <li><a href="#outline">Project Outline</a></li>
    <li><a href="#intro">Project Introduction</a></li>
    <li><a href="#q1">Question 1: Finding Fixed Food Dot using Depth First Search</a></li>
    <li><a href="#q2">Question 2: Breadth First Search</a></li>
    <li><a href="#q3">Question 3: Varying the Cost Function</a></li>
    <li><a href="#q4">Question 4: A* search</a></li>
    <li><a href="#q5">Question 5: Finding All the Corners</a></li>
    <li><a href="#q6">Question 6: Corners Problem: Heuristic</a></li>
    <li><a href="#q7">Question 7: Eating All The Dots</a></li>
    <li><a href="#q8">Question 8: Suboptimal Search</a></li>
    <li><a href="#contributors">Contributors</a></li>
</ol>

<h1 id="intro">Introduction 📝</h1>
This code implements general search algorithms such as depth-first, breadth-first, uniform cost, and A* to optimize Pacman's navigation in a maze world, enabling him to efficiently collect food and reach specific locations.

<br>

<h1 id="q1">🚩 Question 1: Finding Fixed Food Dot using Depth First Search</h1>

<p align="center">
<img src="./gifs/dfs.gif" width="500"></img>
</p>
In this problem, pacman should find a path to reach a <strong>Food Dot</strong>, each step will cost pacman 1.
We implemented the Depth First Search algorithm in <code>search.py</code> in the corresponding function.

We create a <code>DFSNode</code> class to store the state | action | parent, of each state in the problem.
In addition, we created the function <code>get_path</code> in <code>DFSNode</code>, allowing us to reconstruct the path from root to that node.

<h2>Answers to Questions:</h2>
<ol>
    <li>
        <strong>
        Is the exploration order what you
    would have expected?
        </strong>
        <br>
        <pre>yes it is</pre>
    </li>
    <li>
        <strong>
        Does Pacman actually go to all the explored squares on his way to the
goal?
        </strong>
        <br>
        <pre>No, there might exists an explored square that is not located on the root-to-goal path</pre>
    </li>
    <li>
        <strong>
        Is a 130 a least cost solution for <code>mediumMaze</code>? If not, think about what depth-first search is doing wrong.
        </strong>
        <br>
        <pre>No, it is not a least cost solution, DFS returns the first path root-to-goal that it finds without it being an optimal solution</pre>
    </li>

</ol>

<h2>Test Cases</h2>

<pre>$ python pacman.py -l tinyMaze -p SearchAgent</pre>

<li>
Path found with total cost of 10 in 0.0 seconds
</li>
<li>
Search nodes expanded: 15
</li>
<li>
Pacman emerges victorious! Score: 500
</li>

<hr>
<pre>$ python pacman.py -l mediumMaze -p SearchAgent</pre>

<li>
Path found with total cost of 130 in 0.0 seconds
</li>
<li>
Search nodes expanded: 146
</li>
<li>
Pacman emerges victorious! Score: 380
</li>

<hr>
<pre>$ python pacman.py -l bigMaze -p SearchAgent</pre>

<li>
Path found with total cost of 210 in 0.0 seconds
</li>
<li>
Search nodes expanded: 390
</li>
<li>
Pacman emerges victorious! Score: 300
</li>

<br>
<br>

<h1 id="q2">🚩 Question 2: Breadth First Search</h1>

<p align="center">
<img src="./gifs/bfs.gif" width="500"></img>
</p>
In this problem, pacman should find a path to reach a <strong>Food Dot</strong>, each step will cost pacman 1.
We implemented the Breadth First Search algorithm in <code>search.py</code> in the corresponding function.

We create a <code>BFSNode</code> class to store the state | action | parent, of each state in the problem.
In addition, we created the function <code>get_path</code> in <code>BFSNode</code>, allowing us to reconstruct the path from root to that node.

<h2>Answers to Questions:</h2>
<ol>
    <li>
        <strong>
        Does BFS find a least cost solution?
        </strong>
        <br>
        <pre>yes it does</pre>
    </li>

</ol>

<h2>Test Cases</h2>

<pre>$ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs</pre>

<li>
Path found with total cost of 68 in 0.0 seconds
</li>
<li>
Search nodes expanded: 269
</li>
<li>
Pacman emerges victorious! Score: 442
</li>

<hr>
<pre>$ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5</pre>

<li>
Path found with total cost of 210 in 0.0 seconds
</li>
<li>
Search nodes expanded: 620
</li>
<li>
Pacman emerges victorious! Score: 300
</li>

<br>
<br>
<br>

<h2>Generic BFS works on <code>eightpuzzle.py</code></h2>

<pre>$ python eightpuzzle.py</pre>

## A random puzzle

## | 1 | 2 | 5 |

## | 3 | 7 | 4 |

## | 6 | X | 8 |

BFS found a path of 5 moves: ['up', 'right', 'up', 'left', 'left']
After 1 move: up

---

## | 1 | 2 | 5 |

## | 3 | X | 4 |

## | 6 | 7 | 8 |

Press return for the next state...
After 2 moves: right

---

## | 1 | 2 | 5 |

## | 3 | 4 | X |

## | 6 | 7 | 8 |

Press return for the next state...
After 3 moves: up

---

## | 1 | 2 | X |

## | 3 | 4 | 5 |

## | 6 | 7 | 8 |

Press return for the next state...
After 4 moves: left

---

## | 1 | X | 2 |

## | 3 | 4 | 5 |

## | 6 | 7 | 8 |

Press return for the next state...
After 5 moves: left

---

## | X | 1 | 2 |

## | 3 | 4 | 5 |

## | 6 | 7 | 8 |

<br>
<br>
<br>

<h1 id="q3">🚩 Question 3: Varying the Cost Function</h1>

<p align="center">
<img src="./gifs/ucs.gif" width="500"></img>
</p>
In this problem, pacman should find a path to reach a <strong>Food Dot</strong>, each step will cost pacman some value pre-defined by the <code>costFn</code> function.

We implemented the Uniform Cost Search algorithm in <code>search.py</code> in the corresponding function.

We create a <code>UCSSearchProblemNode</code> class to store the state | action | parent and the cost of the path from the root to that node, of each state in the problem i.e. <code>g(n)</code>.

In addition, we created the function <code>get_path</code> in <code>UCSSearchProblemNode</code>, allowing us to reconstruct the path from root to that node.

<h2>Test Cases</h2>

<pre>$ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs</pre>

<li>
Path found with total cost of 68 in 0.0 seconds
</li>
<li>
Search nodes expanded: 269
</li>
<li>
Pacman emerges victorious! Score: 442
</li>

<hr>
<pre>$ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent</pre>

<li>
Path found with total cost of 1 in 0.0 seconds
</li>
<li>
Search nodes expanded: 186
</li>
<li>
Pacman emerges victorious! Score: 646
</li>

<hr>
<pre>$ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent</pre>

<li>
Path found with total cost of 68719479864 in 0.0 seconds
</li>
<li>
Search nodes expanded: 108
</li>
<li>
Pacman emerges victorious! Score: 418
</li>
<br>
<br>
<br>

<h1 id="q4">🚩 Question 4: A* search</h1>

<p align="center">
<img src="./gifs/aStar.gif" width="500"></img>
</p>

We implemented the A\* search algorithm in <code>search.py</code> in the corresponding function.

We create a <code>AStarNode</code> class to store the state | action | parent and the cost of the path from the root to that node, of each state in the problem + the heuristic value of that state i.e. <code>g(n) + h(n)</code>.

<h2>Test Cases</h2>

<pre>$ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic</pre>

<li>
Path found with total cost of 210 in 0.0 seconds
</li>
<li>
Search nodes expanded: 549
</li>
<li>
Pacman emerges victorious! Score: 300
</li>

<br>
<br>
<br>
<h2>Answers to Questions:</h2>
<ol>
    <li>
        <strong>
        What happens on <code>openMaze</code> for the various search
strategies?
        </strong>
        <ul>
            <li> DFS: <br>
                DFS is not optimal, it will not find the shortest path to the goal, it will find the first path to the goal. <br>
                <ul>
                    <li>Path found with total cost of 298 in 0.0 seconds </li>
                    <li>Search nodes expanded: 576</li>
                    <li>Pacman emerges victorious! Score: 212</li>
                </ul>
            </li>
            <li> BFS: <br>
                BFS is optimal, it will find the shortest path to the goal. <br>
                <ul>
                    <li>Path found with total cost of 54 in 0.0 seconds </li>
                    <li>Search nodes expanded: 682</li>
                    <li>Pacman emerges victorious! Score: 456</li>
                </ul>
            </li>
            <li> UCS: <br>
                UCS is optimal, it will find the shortest path to the goal. <br>
                <ul>
                    <li>Path found with total cost of 54 in 0.0 seconds </li>
                    <li>Search nodes expanded: 682</li>
                    <li>Pacman emerges victorious! Score: 456</li>
                </ul>
            </li>
            <li> A*<br>
                A* is optimal, it will find the shortest path to the goal. <br>
                <ul>
                    <li>Path found with total cost of 54 in 0.0 seconds </li>
                    <li>Search nodes expanded: 550</li>
                    <li>Pacman emerges victorious! Score: 456</li>
                </ul>
            </li>
        </ul>
    </li>

</ol>
<br>
<br>
<br>

<h1 id="q5">🚩 Question 5: Finding All the Corners</h1>

<p align="center">
<img src="./gifs/fourCorners.gif" width="500"></img>
</p>

In this problem, pacman should find a path to reach all the <strong>Corners</strong> in the maze, each step will cost pacman some value pre-defined by the <code>costFn</code> function.

We used <pre>self.startState = self.CornersState(self.startingPosition, [False, False, False, False])</pre>
as a representation of the start state, where the boolean values represent if the corner is visited or not.

We implemented the <code>CornersProblem</code> class in <code>searchAgents.py</code> to represent the problem.
Inside that class we created a <code>CornersState</code> class to represent the state of the problem, which is a tuple of the current position and boolean values representing if the corner is visited or not.

We implemented the <code>getSuccessors</code> function to return the successors of the current state, the <code>isGoalState</code> function to check if the current state is the goal state and the <code>getStartState</code> function to return the start state of the problem.

<h2>Test Cases</h2>

<pre>$ python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem</pre>

<li>
Path found with total cost of 28 in 0.0 seconds
</li>
<li>
Search nodes expanded: 252
</li>
<li>
Pacman emerges victorious! Score: 512
</li>

<hr>
<pre>$ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem</pre>

<li>
Path found with total cost of 106 in 0.0 seconds
</li>
<li>
Search nodes expanded: 1966
</li>
<li>
Pacman emerges victorious! Score: 434
</li>

<hr>
<br>
<br>
<br>

<h1 id="q6">🚩 Question 6: Corners Problem: Heuristic</h1>
<p align="center">
<img src="./gifs/q6.gif" width="500"></img>
</p>
In this problem, we implemented the <code>cornersHeuristic</code> function in <code>searchAgents.py</code> to return the heuristic value of the current state.

We created a <code>Admissible</code> and <code>Consistent</code> heuristic function <code>heuristic_found_by_ga_for_corners_problem</code> found in <code>searchAgents.py</code>

<ol>
<li><h2>How we created it:</h2>
<h2><strong>Genetic Algorithm</strong></h2>
We used a genetic algorithm to find the best heuristic function.

<h3><strong>Try it yourself:</strong></h3>
In <code>genetic_algorithm.py</code> you can modify on which maze you want to train ("tinyCorners", "mediumCorners", "bigCorners")
<br>
To run:
<pre>python install -r requirements.txt</pre>
<pre>python genetic_algorithm.py -p CornersProblem -l mediumCorners</pre>

<h3><strong>How it works:</strong></h3>
<ol>
<li> <strong>Encoding</strong></li>
A chromosome is a set of 0 and 1 (i.e. <code>010011</code>) where each digit, represent whether its corresponding heuristic is used.<br>
The full list of heuristic functions is:
<pre>
    HEURISTICS_LIST = [
        manhattan_distance,
        euclidean_distance,
        diagonal_distance,
        max_heuristic,
        min_heuristic,
        null_heuristic
    ]
</pre>
How? look  at the below example:
<pre>010011</pre>
means that
<pre>euclidean_distance,  min_heuristic,  null_heuristic</pre>
are being used
<br>
<br>
<br>
<li> <strong>Fitness Function </strong></li>
To evaluate the fitness of a chromosome, we ran aStarSrarch on the problem where the heuristic used is <code>new_heuristic</code> and we returned:<br>
<pre>(1/nodes_expanded)*(10**c)</pre>
Where c is a small integer just to make even small changes in nodes_expanded a more valuable thing to the algorithm

<br>
<code>new_heuristic</code> is defined as follow (pseudo code):
<pre>
def new_heuristic(start, goal):
    set_of_heuristic_allowed = extract_allowed_heuristics(chromosome)
    values = [h(start, goal) for h in set_of_heuristic_allowed]
    return method_of_joining_heuristics(values)
</pre>

where <code>method_of_joining_heuristics</code> is one of:
<pre>
    method_of_joining_heuristics = {
        'max' : max,
        'min' : min,
        'mean' : lambda x: sum(x)/len(x),
        'mode' : lambda x: max(set(x), key=x.count),
        'median' : lambda x: median(x),
        'range': lambda x: max(x) - min(x),
    }
</pre>
<li><strong>Selection</strong></li>
We used <code>ranking selection</code> to select the best heuristic functions.

<li> <strong>Crossover</strong> </li>
We used <code>single point crossover</code> to create new heuristic functions. Crossover probability is 0.8.

<li> <strong>Mutation</strong> </li>
We used <code>bitstring mutation</code> to mutate the heuristic functions allowed. Mutation probability is 0.2.

<li> <strong>Stopping Criteria</strong> </li>
We used <code>number of generations</code> as a stopping criteria. We ran the genetic algorithm for 30 generations.

<li> <strong>Results</strong> </li>
We ran the genetic algorithm for 30 generations and the best heuristic function we found is:
<pre>
Best solution:   (1, 1, 1, 1, 1, 1)
</pre>

<pre>
Best Fitness:    1
</pre>

<pre>
Best Cost (number of nodes expanded):    741
</pre>

<pre>
Best solution is made of:       RANGE( manhattan_distance,  euclidean_distance,  diagonal_distance,  max_heuristic,  min_heuristic,  null_heuristic,  )
</pre>
Where
<pre>
RANGE = lambda x: max(x) - min(x)
</pre>
thus the best heuristic combination is <code>RANGE( manhattan_distance,  euclidean_distance,  diagonal_distance,  max_heuristic,  min_heuristic,  null_heuristic,  )</code>

</ol>
</li>
<li><h2>How we used it:</h2>
In <code>searchAgents.py</code> in the function <code>cornerHeuristic</code>, we generated all the permutations of the cornerns i.e. ((c1, c2, c3, c4), (c2, c4, c1, c3) . . .) <br>
Then for each of those permutations we used our <code>heuristic_found_by_ga_for_corners_problem</code> to calculate the total path cost of that permutation. Then we return the minimum path cost of a permutation.<br>
Pseudo Code:
<pre>
min_cost = infinity
for permutation in permutations_of_corners:
    cost = 0
    for i in range(len(permutations_of_corners)-1):
        cost += heuristic_found_by_ga_for_corners_problem(perm[i], perm[i+1])
    if cost < min_cost:
        min_cost = cost
</pre>
</li>
</ol>

<h2>Test Cases</h2>

<pre>$ python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5</pre>

<li>
Path found with total cost of 106 in 0.1 seconds
</li>
<li>
Search nodes expanded: 741
</li>
<li>
Pacman emerges victorious! Score: 434.0
</li>

<hr>

<br>

<pre>$ python pacman.py -l bigCorners -p AStarCornersAgent -z 0.5</pre>

<li>
Path found with total cost of 162 in 0.2 seconds
</li>
<li>
Search nodes expanded: 1725
</li>
<li>
Pacman emerges victorious! Score: 378.0
</li>

<hr>

<br>
<br>
<br>

<h1 id="q7">🚩 Question 7: Eating All The Dots</h1>
<p align="center">
<img src="./gifs/q7.gif" width="500"></img>
</p>
In this problem, we implemented the <code>foodHeuristic</code> function in <code>searchAgents.py</code> to return the heuristic value of the current state.

We created a <code>Admissible</code> and <code>Consistent</code> heuristic function.

<h2>How it Works:</h2>
We also used the genetic algorithm to find the best heuristic function for this problem. <br>
The function is <code>heuristic_found_by_ga_for_food_problem</code> <br>
We created a <code>exactDistanceUsingAStar(start, goal)</code> function that returns the actual cost of the path from the start to the goal using the <code>AStarSearch</code> algorithm and <code>heuristic_found_by_ga_for_food_problem</code><br>
Then we found <code>closest_food</code> and <code>furthest_food</code> using <code>heuristic_found_by_ga_for_food_problem</code> <br>
Then we returned the heuristic value as:

<pre>
    return exactDistanceUsingAStar(start, closest_food) + heuristic_found_by_ga_for_food_problem(closest_food, furthest_food)
</pre>

<h2>Genetic Algorithm Results:</h2>
We ran the genetic algorithm for 30 generations using <br>
<pre>python install -r requirements.txt</pre>
<pre>
python genetic_algorithm.py -p FoodSearchProblem -l trickySearch
</pre>
and the best heuristic function we found is:
<pre>
Best solution:   (0, 0, 1, 1, 1, 0)
Best Fitness:    24
Best Cost (number of nodes expanded):    4089
Best solution is made of:       MAX( diagonal_distance,  max_heuristic,  min_heuristic,  )
</pre>

<h2>Test Cases</h2>

<pre>$ python pacman.py -l trickySearch -p AStarFoodSearchAgent</pre>

<li>
Path found with total cost of 60 in 1.4 seconds
</li>
<li>
Search nodes expanded: 4089
</li>
<li>
Pacman emerges victorious! Score: 570
</li>

<hr>
<pre>$ python pacman.py -l mediumSearch -p AStarFoodSearchAgent</pre>

<li>
Was not able to solve it in 30 seconds (i.e. timeout . . .)
</li>

<hr>
<br>
<br>
<br>

<h1 id="q8">🚩 Question 8: Suboptimal Search</h1>
<p align="center">
<img src="./gifs/q8.gif" width="500"></img>
</p>
In this section, we created an agent  that  always  greedily  eats  the  closest  dot. Using <code>ClosestDotSearchAgent</code> in searchAgents.py, we implemented a function that finds a path to the closest dot <code>findPathToClosestDot</code>

We used <code>BFS</code> to find the path to the closest dot using <code>AnyFoodSearchProblem</code> as gameState for <code>BFS</code>.

We modified in <code>AnyFoodSearchProblem</code> the function <code>isGoalState</code> to return true if the current state is a food.

<h2>Test Cases</h2>

<pre>$ python pacman.py -l bigSearch -p AStarFoodSearchAgent</pre>

<li>
Path found with total cost of 350.
</li>
<li>
Pacman emerges victorious! Score: 2360
</li>

<hr>
<br>
<br>
<pre>$ python pacman.py -l mediumSearch -p AStarFoodSearchAgent</pre>

<li>
Path found with total cost of 171.
</li>
<li>
Pacman emerges victorious! Score: 1409
</li>

<hr>

<h1 id="contributors">Contributors 📖</h1>

<ul>
<li>Charbel Fayad - charbel.fayad01@lau.edu - 202102394</li>
<li>Manel Roumaissa Benabid - manelroumaissa.benabid@lau.edu - 201906232</li>
</ul>

<h1 id="license">License 📄</h1>

This project is licensed under the MIT License - see the <a href="MIT License">LICENSE.md</a> file for details
