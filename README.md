# 📈👣 [bellman-ford-shortest-path](./bellman-ford-shortest-path/)
A cs-320 coding project that computes two non-overlapping optimal paths in an undirected graph using the Bellman-Ford algorithm: first from a start vertex to a remote vertex, then back to the start without reusing edges.  
It handles graphs with positive edge weights and requires bidirectional edges for undirected traversal (e.g., separate `A→B` and `B→A` edges). 

## Run
Define your graph in a file, parse it with `parse_graph_file`, specify `start` and `remote` vertices, and run `bellman_ford(graph, start, remote)` to get the paths as tuples of `EdgeEL` objects (or `(None, None)` if invalid):  
```python  
graph = parse_graph_file("graph.txt")  
path_to, path_from = bellman_ford(graph, VertexEL("A"), VertexEL("B"))  
```

# 🎲#️⃣ [creating-random-distribution](./creating-random-distribution/)

# 🕳️🔎 [depth-first-search](./depth-first-search/)

# 🧬📈 [genetic-TSP](./genetic-TSP/)

# 🔀🗄️ [heapsort](./heapsort/)

# 📖🆔 [palindrome-identifier](./palindrome-identifier/)

# 📕📘 [tuple-word-comparisons](./tuple-word-comparisons/)
