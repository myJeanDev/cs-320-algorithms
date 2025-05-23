# 📈👣 [bellman-ford-shortest-path](./bellman-ford-shortest-path/)
**python code using the Bellman-Ford algorithm**  

Computes two non-overlapping optimal paths in an undirected graph: first from a start vertex to a remote vertex, then back to the start without reusing edges.  
It handles graphs with positive edge weights and requires bidirectional edges for undirected traversal (e.g., separate `A→B` and `B→A` edges). 

If you want to run the code:  
Define your graph in a file, parse it with `parse_graph_file`, specify `start` and `remote` vertices, and run `bellman_ford(graph, start, remote)` to get the paths as tuples of `EdgeEL` objects (or `(None, None)` if invalid):  

```python  
graph = parse_graph_file("graph.txt")  
path_to, path_from = bellman_ford(graph, VertexEL("A"), VertexEL("B"))  
```

# 🎲#️⃣ [creating-random-distribution](./creating-random-distribution/)
**python code for equal random distribution**  

The code assigns players to valid positions on a grid-based field, divided into left (green team) and right (gold team) halves.  
Ensures no overlapping placements, and returns tuples of positions for each team. The algorithm prioritizes available grid cells (marked as `True`/1) and handles collisions by retrying (naive solution), efficiently distributing players while respecting team zones. Requires a square grid and returns empty tuples for invalid inputs.

# 🕳️🔎 [depth-first-search](./depth-first-search/)  
**python code for depth-first search**  

Traverses a graph data structure using an edge list representation.

# 🧬📈 [genetic-TSP](./genetic-TSP/)
**python Genetic Algorithm to solve the Traveling Salesman Problem**  

The goal is to find the shortest possible route that visits each city exactly once (a Hamiltonian circuit) and returns to the starting point. The algorithm evolves a population of candidate paths over generations, using fitness-based selection, crossover, and mutation.

# 🔀🗄️ [heapsort](./heapsort/)
**python code for a Heapsort algorithm**  

`O(n log n)` time complexity. `max_heapify()` to maintain the max-heap property, `build_max_heap()` to transform an unsorted list into a valid max-heap, and `heapsort` as the entry point for sorting. The algorithm works by iteratively extracting the maximum element from the heap, reducing the heap size, and reconstructing the heap until the entire list is sorted. Uses in-place heap operations for memory efficiency. Returns a new sorted list in ascending order.

# 📖🆔 [palindrome-identifier](./palindrome-identifier/)
**python code that converts tuples into palindromes**  

It splits the input into halves, reverses one half, and iteratively adjusts the segments by removing mismatched elements until a palindrome is found or a recursion limit is reached. The algorithm prioritizes removing elements from the longer segment when adjacent matches are detected, and attempts the process again on the reversed pattern if the initial pass fails.

# 📕📘 [tuple-word-comparisons](./tuple-word-comparisons/)
**python code to create tuple from the difference of two tuples**  
Returns words present in one tuple `(words)` but not in another `(wordlist)`, with case insensitivity and de-duplication. The function first validates that both inputs are non-null tuples, converts all elements to lowercase, sorts them alphabetically, and removes duplicates. Then it checks for differences using binary search. The result is a tuple of unique, lowercase words from words that are absent in wordlist, sorted lexicographically. Any invalid inputs return None.
