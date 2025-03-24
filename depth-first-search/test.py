import edgegraph
import random
from main import dfs
import time
import os


def test():
    graph = diamond_graph()
    start_time = time.time()
    print(dfs(graph, random.choice(graph.vertices())))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")

def simple_graph():
        # Create vertices
    vertex_a = edgegraph.VertexEL("A")
    vertex_b = edgegraph.VertexEL("B")
    vertex_c = edgegraph.VertexEL("C")
    vertex_d = edgegraph.VertexEL("D")
    vertex_e = edgegraph.VertexEL("E")

    # Create edges
    edge_ab = edgegraph.EdgeEL("edge_A_B", vertex_a, vertex_b)
    edge_ac = edgegraph.EdgeEL("edge_A_C", vertex_a, vertex_c)
    edge_bd = edgegraph.EdgeEL("edge_B_D", vertex_b, vertex_d)
    edge_be = edgegraph.EdgeEL("edge_B_E", vertex_b, vertex_e)

    # Create the graph
    graph = edgegraph.GraphEL()

    # Add vertices to the graph
    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)
    graph.add_vertex(vertex_d)
    graph.add_vertex(vertex_e)

    # Add edges to the graph
    graph.add_edge(edge_ab)
    graph.add_edge(edge_ac)
    graph.add_edge(edge_bd)
    graph.add_edge(edge_be)

def diamond_graph():
    # Create vertices
    vertex_a = edgegraph.VertexEL("A")
    vertex_b = edgegraph.VertexEL("B")
    vertex_c = edgegraph.VertexEL("C")
    vertex_d = edgegraph.VertexEL("D")

    # Create edges
    edge_ab = edgegraph.EdgeEL("edge_A_B", vertex_a, vertex_b)  # A -> B
    edge_ac = edgegraph.EdgeEL("edge_A_C", vertex_a, vertex_c)  # A -> C
    edge_bd = edgegraph.EdgeEL("edge_B_D", vertex_b, vertex_d)  # B -> D
    edge_cd = edgegraph.EdgeEL("edge_C_D", vertex_c, vertex_d)  # C -> D

    # Create the graph
    graph = edgegraph.GraphEL()

    # Add vertices to the graph
    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)
    graph.add_vertex(vertex_d)

    # Add edges to the graph
    graph.add_edge(edge_ab)
    graph.add_edge(edge_ac)
    graph.add_edge(edge_bd)
    graph.add_edge(edge_cd)

    return graph


test()