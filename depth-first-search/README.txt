LAB 6:
    Depth First Search

Methods:
    dfs(graph: GraphEL, start: VertexEL)
        returns tuple(VertexEL) in a valid DFS order

Assume:
    - Graph is a single connected tree
    - Graph = None, return an empty tuple()
    - start = None, return an empty tuple()
    - start is not inside of graph, return an empty tuple()

Time Complexity:
    O(vertices + edges)
