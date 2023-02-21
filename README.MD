<h1 align="center">Pacman Search
    <img src="./gifs/200w.webp" width="40">
</h1>

<h3 align="center"> CSC460 - Artificial Intelligence ©️</h3>
<h5 align="center"> Project Phase 1 </h5>

<p align="center"> 
  <img src="./gifs/big.gif" alt="Animated gif pacman game" height="282px" width="550" style="border-radius:2rem">
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

<h1 id="q1">🚩 Question 1: Finding Fixed Food Dot using Depth First Search</h1>

<video src="./gifs/dfs_medium_maze.mp4"></video>

We implemented the Depth First Search algorithm in <code>search.py</code> in the corresponding function.

We create a <code>DFSSearchProblemNode</code> class to store the state | action | parent, of each state in the problem.
In addition, we created the function <code>get_path</code> in <code>DFSSearchProblemNode</code>, allowing us to reconstruct the path from root to that node.

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
<pre>$ python pacman.py -l tinyMaze -p SearchAgent</pre>

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
<h1 id="q3">🚩 Question 3: Varying the Cost Function</h1>
<h1 id="q4">🚩 Question 4: A* search</h1>
<h1 id="q5">🚩 Question 5: Finding All the Corners</h1>
<h1 id="q6">🚩 Question 6: Corners Problem: Heuristic</h1>
<h1 id="q7">🚩 Question 7: Eating All The Dots</h1>
<h1 id="q8">🚩 Question 8: Suboptimal Search</h1>

<h1 id="contributors">Contributors 📖</h1>

<ul>
<li>Charbel Fayad - charbel.fayad01@lau.edu - 202102394</li>
<li>Manel Benabid - manel.benabid@lau.edu - </li>
</ul>
