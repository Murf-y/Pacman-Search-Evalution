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

## A random puzzle:

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
            <li> A* <br>
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
<h1 id="q6">🚩 Question 6: Corners Problem: Heuristic</h1>
<h1 id="q7">🚩 Question 7: Eating All The Dots</h1>
<h1 id="q8">🚩 Question 8: Suboptimal Search</h1>

<h1 id="contributors">Contributors 📖</h1>

<ul>
<li>Charbel Fayad - charbel.fayad01@lau.edu - 202102394</li>
<li>Manel Benabid - manel.benabid@lau.edu - </li>
</ul>
