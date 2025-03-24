from edgegraph import GraphEL, VertexEL


def is_valid_input(graph: GraphEL, start: VertexEL) -> bool:
    if graph is None or start is None:
        return False
    if start not in graph.vertices():
        return False
    return True


def dfs(graph: GraphEL, start: VertexEL) -> tuple:
    if not is_valid_input(graph, start):
        return ()
    
    dfs_path: list[VertexEL] = []
    visited_vertices: set[str] = set()
    stack: list[VertexEL] = [start]

    while stack:
        current_vertex: VertexEL = stack.pop()
        
        for neighbor in graph.adjacent_vertices(current_vertex):
            if neighbor.name not in visited_vertices:
                stack.append(neighbor)
        
        if current_vertex.name not in visited_vertices:
            dfs_path.append(current_vertex)
            visited_vertices.add(current_vertex.name)
    return tuple(dfs_path)
