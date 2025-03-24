Lab 7
"Out and Back with Bellman-Ford"
Using the Bellman-Ford algorithm, find the shortest path to remote, then find a different shortest path back to the start.  

bellman_ford(graph, start, end) -> list:  
Return Values:
- The first tuple represents the shortest path between start and remote.  
- The second tuple is the shortest path from remote back to start.  
All the edges should be different from the edges in the first tuple.  
Each tuple is a list of edges

Assume:
 - assume the graph is not a forest
 - Edges are undirected
 - Edges have weights

Input Validation:
 - If Graph == None: return None, None
 - When exploring the graph, if encounter a 0 or > 0 weight for an edge, return None, None
 - If start or remote is None: return None, None
 - If start or remote is not in graph: return None, None
 - If there is a shortest path to remote but then no disjoint path back, you should return the outbound shortest path for the first return value and None for the second.

 Big-O:
 O(Vertices * Edges)