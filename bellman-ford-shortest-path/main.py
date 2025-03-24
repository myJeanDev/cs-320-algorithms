from edgegraph import *
import copy


def is_valid_input(graph, start, remote) -> bool:
    if graph is None:
        return False
    for each in graph.edges():
        if each.get_value() <= 0:
            return False

    if start is None or remote is None:
        return False

    is_start = False
    is_remote = False
    for each in graph.vertices():
        if start.name == each.name:
            is_start = True
        if remote.name == each.name:
            is_remote = True
    
    if not is_start or not is_remote:
        return False
    
    return True


def find_optimal_path(predecessors, start, remote):
    print("finding paths from:")
    print(predecessors)
    # when an edge is used, it cannot be used again
    path = []
    current_node = remote
    visited = set()

    while current_node.name != start.name:
        if current_node.name in visited:
            return None
        visited.add(current_node.name)

        if predecessors.get(current_node.name) is not None:
            edge_to_previous = predecessors[current_node.name]
            path.append(edge_to_previous)
            current_node = edge_to_previous.tail()
            print(f"go to {current_node}, path: {path}")
        else:
            return None
    
    path.reverse()
    print("\npath:")
    print(path)
    print("\n")
    return tuple(path)


def relax_edge(predecessors, node_from, node_to, edge):
    new_value = node_from.get_value() + edge.get_value()
    if new_value < node_to.get_value():
        node_to.set_value(new_value)
        
        if edge.tail() == node_from:
            predecessors[node_to.name] = edge
        else:
            # Edge is facing wrong way, create a new one that is correct
            predecessors[node_to.name] = EdgeEL(edge.name, node_from, node_to)


def destress_graph(graph: GraphEL, start: VertexEL) -> dict[str: EdgeEL]:
    infinity = float("Inf")
    for each in graph.vertices():
        each.set_value(infinity)
    start.set_value(0)

    # dictionary that uses names to hash
    # holds the last edge thats the best path to this node from the start
    predecessors: dict[str: EdgeEL] = {}
    for each in graph.vertices():
        predecessors[each.name] = None

    for _ in range(len(graph.vertices()) - 1):
        for vertex in graph.vertices():
            for edge in graph.incident(vertex):
                node_a, node_b = edge.ends()
                relax_edge(predecessors, node_b, node_a, edge)
                relax_edge(predecessors, node_a, node_b, edge)
    print(predecessors)
    return predecessors


def remove_all_edges(graph: GraphEL, edges: list[EdgeEL]) -> GraphEL:
    print(f"edges to remove {edges}")
    for edge in edges:
        if edge is not None:
            remove_undirected_edge(graph, edge.head(), edge.tail(), edge.get_value())
    return graph


def remove_undirected_edge(graph: GraphEL, vertex_a, vertex_b, edge_weight):
    edge_one = graph.get_edge_with_ends(vertex_a, vertex_b)
    if edge_one and edge_one.get_value() == edge_weight:
        graph.rm_edge(edge_one)

    edge_two = graph.get_edge_with_ends(vertex_b, vertex_a)
    if edge_two and edge_two.get_value() == edge_weight:
        graph.rm_edge(edge_two)


def bellman_ford(graph: GraphEL, start: VertexEL, remote: VertexEL) -> list[tuple]:

    if not is_valid_input(graph, start, remote):
        return None, None
    
    new_graph = copy.deepcopy(graph)
    path_start_to_remote = []
    path_remote_to_start = []
    start_name = new_graph.get_vertex(start.name)
    remote_name = new_graph.get_vertex(remote.name)

    # path (start) --> (remote)
    best_edges: dict[str: EdgeEL] = destress_graph(new_graph, start_name)
    path_start_to_remote = find_optimal_path(best_edges, start_name, remote_name)
    new_graph = remove_all_edges(new_graph, path_start_to_remote)

    print(new_graph)

    # path (remote) --> (start)
    back_best_edges: dict[str: EdgeEL] = destress_graph(new_graph, remote_name)
    path_remote_to_start = find_optimal_path(back_best_edges, remote_name, start_name)

    return path_start_to_remote, path_remote_to_start
