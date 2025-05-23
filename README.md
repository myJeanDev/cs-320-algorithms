# 📈👣 [bellman-ford-shortest-path](./bellman-ford-shortest-path/)
Code that computes two non-overlapping optimal paths in an undirected graph using the Bellman-Ford algorithm: first from a start vertex to a remote vertex, then back to the start without reusing edges.  
It handles graphs with positive edge weights and requires bidirectional edges for undirected traversal (e.g., separate `A→B` and `B→A` edges). 

## Run
Define your graph in a file, parse it with `parse_graph_file`, specify `start` and `remote` vertices, and run `bellman_ford(graph, start, remote)` to get the paths as tuples of `EdgeEL` objects (or `(None, None)` if invalid):  
```python  
graph = parse_graph_file("graph.txt")  
path_to, path_from = bellman_ford(graph, VertexEL("A"), VertexEL("B"))  
```

# 🎲#️⃣ [creating-random-distribution](./creating-random-distribution/)
Code that randomly assigns players in an equal distribution to valid positions on a grid-based field, divided into left (green team) and right (gold team) halves.  
Ensures no overlapping placements, and returns tuples of positions for each team. The algorithm prioritizes available grid cells (marked as `True`/1) and handles collisions by retrying (naive solution), efficiently distributing players while respecting team zones. Requires a square grid and returns empty tuples for invalid inputs.

# 🕳️🔎 [depth-first-search](./depth-first-search/)

# 🧬📈 [genetic-TSP](./genetic-TSP/)

# 🔀🗄️ [heapsort](./heapsort/)

# 📖🆔 [palindrome-identifier](./palindrome-identifier/)

# 📕📘 [tuple-word-comparisons](./tuple-word-comparisons/)
