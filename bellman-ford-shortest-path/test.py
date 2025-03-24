from main import *
from edgegraph import *

def test():
    testing_graph = parse_graph_file("/Users/willschmitz/github-projects/school-projects/2024/CS-320/lab_seven/graph.txt")
    testing_start = testing_graph.get_vertex("0")
    testing_end = testing_graph.get_vertex("5")
    print(bellman_ford(testing_graph, testing_start, testing_end))


def parse_graph_file(file_path):
    graph = GraphEL()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("%") or not line:
                continue

            parts = line.split()
            if parts[0] == 'n':
                # Parse a vertex
                _, x, y, name = parts
                vertex = VertexEL(name)
                graph.add_vertex(vertex)
            elif parts[0] == 'e':
                # Parse an edge
                _, v1_name, v2_name, edge_name, weight = parts
                v1_name, v2_name = v1_name, v2_name
                edge_name = edge_name
                weight = float(weight)

                # Get or create vertices
                vertex1 = graph.get_vertex(v1_name) if v1_name in graph._vertices else VertexEL(v1_name)
                vertex2 = graph.get_vertex(v2_name) if v2_name in graph._vertices else VertexEL(v2_name)

                # Add vertices to the graph
                graph.add_vertex(vertex1)
                graph.add_vertex(vertex2)

                # Create and add edge to the graph
                edge = EdgeEL(edge_name, vertex1, vertex2)
                edge.set_value(weight)
                graph.add_edge(edge)

    return graph

test()