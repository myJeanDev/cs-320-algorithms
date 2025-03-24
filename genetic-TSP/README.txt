Traveling Salesperson Problem: Using a genetic algorithm
---
_In this lab, you are tasked with writing the critical portions of a genetic algorithm to solve the traveling salesperson problem (TSP)._
Specifically you will write a
routine ga_tsp(initial_population, distances, generations) which is given an initial population of valid Hamiltonian paths
(initial_population, which is a list of paths [tuples])
(distances): Dictionary of distances 
Number of generations (generations) that your algorithm should run.
ga_tsp() should return the best path (a tuple of cities) from the final generation, after completing the requisite number of generations.

Note that a generation is defined as a single iteration of the algorithm (parent selection, crossover, selection of the fittest population) using a steady population across generations (the same number of children as there are parents). If you use a variation of the above approach, such as creating half the number of children compared to the population size, you'll need to perform twice the number of iterations (generations).

Details
A path is a tuple listing all "cities" in the path. It assumed the path is a Hamiltonian circuit that completes by taking an edge from the last city listed back to the first city listed. Do not list the first city twice (at the start and end of the tuple)!

We are providing several supporting routines and files:

util.py contains three utility routines. cost(path, distances) will return the cost of a path. As a debugging aid, cost() checks that the path and distance dictionary are valid and will return None if not (this should cause your code to throw a TypeError if you use the return value). Note that cost() may not detect all invalid paths. valid_path(path) confirms the path is internally sound (no repetitions). best_path(list_of_paths, distances) returns the best (lowest cost) path in list_of_paths.
load_dist(filename) will load a dictionary of distances from the file named filename and can be imported from load_dist.py. The format of filename is individual lines of the form "A, B, distance" where A and B are city names and distance is a positive integer distance. A line causes the distance from A to B and B to A to be loaded into the dictionary. A line starting with # is a comment. Comment lines and blank lines are ignored. load_dist also ensures that the distance from a node to itself is always zero. You can update the A to B (B to A) distance later in the file -- so if you want to slightly change the topology (aka distances), you can just add a custom update to the end of the file. load_dist() returns a list of all the city names and a dictionary of distances. load_dist() returns None, None if the file did not load properly.
tsp.py if run at the command line with a filename, so % python3 tsp.py filename will load distances from filename, compute an initial population, and call ga_tsp() to run 500 generations and report if ga_tsp() found a better result than was in the initial population.
init_pop.py contains two routines to create an initial population. These routines are defined in tsp.py. One version of the routine, init_pop(list, dist), take a list of cities and the distance matrix and generates a random set of initial paths of appropriate size. The other version, init_lousy(), intentionally creates an initial set of paths with high costs -- which may be useful for debugging. (Instructions for using init_lousy() are in the file and in comments in tsp.py).
two_opt.py contains the 2-opt algorithm described in class, designed to use the lab's cost function. You are not required to use 2-opt in your implementation. It is provided solely for your convenience.
We are providing two sample distance files: DIST6-simple is a simple 6 city world with a clear best path. DIST23-basic is a 23 city world divided up into 3 districts (clouds).
More Details
If ga_tsp is given None for any argument it should return None. If generations is not positive, ga_tsp should return None. You can assume distances and initial_population are valid if non-None.

Performance
We have no big-O performance requirements for this assignment. Rather we will run some tests designed to see if your genetic algorithm finds better results than the best path in the initial population (you can assume we'll rig the initial population so a range of better solutions are feasible).

Python Guidance
You may want to use the sorted routine in ways you have not used it before. Specifically, sorted can take a list of additional arguments that may be useful.

To sort a list of paths using the cost function you set the key value in sorted. But sorted assumes the key function takes a single value, the item whose cost is to be assessed. To tell sorted that cost takes two arguments and assign the value of the second argument, you need to import partial from functools and then write something like: sorted(population, key=partial(cost, distances=dist)), where dist is the dictionary of distances. There's an example in init_pop.py.

If you wish, you can also instruct sorted to sort in reverse order (so from high to low) by setting reverse=True. Again, there's an example in init_pop.py.

Zybooks guidance
We are running near the limits of zybooks' testing system to allow you to do this lab. As a result we only get to run 100 generations (vs. the 500+ generations we'd prefer to run). Furthermore, if your genetic algorithm is really slow, zylabs will timeout your tests. So do try to be efficient.

A Caution
This lab is the only lab that is identical to the one assigned last semester. So if you ask your friend who took CS320 last semester for advice, be careful not to look at or copy their code. We will check against last semester's solutions for possible plagiarism.