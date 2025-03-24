#  set of classes to support a Graph class that uses edge list structure

# a vertex in a graph
class VertexEL:
    def __init__(self, name):
        assert name is not None
        self.name = name
        self._value = None

    # set VertexEL value
    def set_value(self, value):
        self._value = value

    # need ability to compare vertexs in lists and such

    def __lt__(self, other):
        if not isinstance(other, VertexEL):
            raise Exception("VertexEL cannot be compared to {type(other)}")
        return self.name < other.name

    def __eq__(self, other):
        if not isinstance(other, VertexEL):
            raise Exception("VertexEL cannot be compared to {type(other)}")
        return self.name == other.name

    def __ne__(self, other):
        return not (self == other)

    # for printing

    def __repr__(self):
        if self._value is None:
            return f"{self.name}"
        return f"{self.name}({self._value})"


# edge in a graph


class EdgeEL:
    def __init__(self, name, v1, v2):
        assert (name is not None) and (v1 is not None) and (v2 is not None)
        self.name = name
        self._value = None
        self._vertex1 = v1
        self._vertex2 = v2

    def set_value(self, value):
        self._value = value

    def ends(self):
        return [self._vertex1] + [self._vertex2]

    # need ability to compare vertices in lists and such

    def __lt__(self, other):
        if not isinstance(other, EdgeEL):
            raise Exception("EdgeEL cannot be compared to {type(other)}")
        return self.name < other.name

    def __eq__(self, other):
        if not isinstance(other, EdgeEL):
            raise Exception("EdgeEL cannot be compared to {type(other)}")
        return self.name == other.name

    def __ne__(self, other):
        return not (self == other)

    # for printing

    def __repr__(self):
        if self._value is None:
            return f"{self.name}[{self._vertex1}-{self._vertex2}]"
        return f"{self.name}({self._value})[{self._vertex1}-{self._vertex2}]"


# graph


class GraphEL:
    def __init__(self):
        self._vertices = {}
        self._edges = {}

    # add new vertex to graph
    # this overwrites if vertex of this name is already present

    def add_vertex(self, vertex):
        self._vertices[vertex.name] = vertex

    def rm_vertex(self, vertex):
        if vertex.name in self._vertices:
            del self._vertices[vertex.name]

    # add new edge to graph.  If edge has unknown vertices, add them
    # to graph

    def add_edge(self, edge):
        self._edges[edge.name] = edge
        for v in edge.ends():
            if v.name not in self._vertices:
                print(f"adding {v.name}")
                self.add_vertex(v)

    def rm_edge(self, edge):
        if edge.name in self._edges:
            del self._edges[edge.name]

    # graph operations from textbook

    def vertices(self):
        return list(self._vertices.values())

    def edges(self):
        return sorted(list(self._edges.values()))

    def num_vertices(self):
        return len(self._vertices)

    def num_edges(self):
        return len(self._edges)

    def incident(self, v):
        il = []
        for e in self.edges():
            if v in e.ends():
                il += [e]
        return il

    def degree(self, v):
        return len(self.incident(v))

    def adjacent_vertices(self, v):
        av = []
        for i in self.edges():
            ie = i.ends()
            if v in ie:
                if ie[0] == v:
                    av += [ie[1]]
                else:
                    av += [ie[0]]
        return av

    def __repr__(self):
        rep = ""
        for edge in self._edges.values():
            rep += str(edge) + "\n"
        return rep


def parse_graph_file(file_path):
    graph = GraphEL()

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue  # Skip invalid lines

            edge_name, v1_name, v2_name = (
                parts[0].strip(),
                parts[1].strip(),
                parts[2].strip(),
            )
            vertex1 = graph._vertices.get(v1_name, VertexEL(v1_name))
            vertex2 = graph._vertices.get(v2_name, VertexEL(v2_name))

            edge = EdgeEL(edge_name, vertex1, vertex2)

            graph.add_vertex(vertex1)
            graph.add_vertex(vertex2)
            graph.add_edge(edge)

    return graph
