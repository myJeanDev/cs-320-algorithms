#  set of classes to support a Graph class that uses edge list structure

# a vertex in a graph
class VertexEL:

    def __init__(self, name):
        assert (name is not None)
        self.name = name
        self._value = None

    # for annotational purposes
    
    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    # need ability to compare vertexs in lists and such

    def __lt__(self, other):
        if not isinstance(other, VertexEL):
            raise Exception(f"VertexEL cannot be compared to {type(other)}")
        return (self.name < other.name)
    
    def __eq__(self, other):
        if not isinstance(other, VertexEL):
            raise Exception(f"VertexEL cannot be compared to {type(other)}")
        return (self.name == other.name)

    def __ne__(self, other):
        return not (self == other)

    # for printing

    def __repr__(self):
        if (self._value is None):
            return f'{self.name}'
        return f'{self.name}({self._value})'

# edge in a graph


class EdgeEL:

    def __init__(self, name, v1, v2):
        assert ((name is not None) and (v1 is not None) and (v2 is not None))
        self.name = name
        self._value = None
        self._vertex1 = v1
        self._vertex2 = v2
        
    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def ends(self):
        return ([self._vertex1] + [self._vertex2])
        
    def tail(self):
        return self._vertex1
    
    def head(self):
        return self._vertex2

    # need ability to compare vertices in lists and such

    def __lt__(self, other):
        if not isinstance(other, EdgeEL):
            raise Exception(f"EdgeEL cannot be compared to {type(other)}")
        return (self.name < other.name)

    def __eq__(self, other):
        if not isinstance(other, EdgeEL):
            raise Exception(f"EdgeEL cannot be compared to {type(other)}")
        return (self.name == other.name)

    def __ne__(self, other):
        return not (self == other)

    # for printing

    def __repr__(self):
        if (self._value is None):
            return f'{self.name}[{self._vertex1}-{self._vertex2}]'
        return f'{self.name}({self._value})[{self._vertex1}-{self._vertex2}]'

# graph


class GraphEL:

    def __init__(self):
        self._vertices = {}
        self._edges = {}

    def delete_edge(self, e):
        edges = [v for _, v in self._edges.items()]
        if e in edges:
            del self._edges[e.name]
    
    def get_edge_with_ends(self, v1, v2):
        edges = [v for _, v in self._edges.items()]
        for edge in edges:
            edge_ends = tuple(edge.ends())
            if edge_ends[0] == v1 and edge_ends[1] == v2:
                return edge
        return None
            
    # vertex methods

    def get_vertex(self, name):
        return self._vertices[name]

    def find_vertex(self, vertex):
        return self._vertices[vertex.name]

    def add_vertex(self, vertex):  # this overwrites if vertex of this name is already present
        self._vertices[vertex.name] = vertex

    def rm_vertex(self, vertex):
        if (vertex.name in self._vertices):
            del self._vertices[vertex.name]

    # edge methods
    
    def get_edge(self, name):
        return self._edges[name]

    def find_edge(self, edge):
        return self._edges[edge.name]

    # add new edge to graph.  If edge has unknown vertices, add them
    # to graph

    def add_edge(self, edge):
        self._edges[edge.name] = edge
        for v in edge.ends():
            if (v.name not in self._vertices):
                print(f"adding {v.name}")
                self.add_vertex(v)

    def rm_edge(self, edge):
        if (edge.name in self._edges):
            del self._edges[edge.name]

    # graph operations from textbook (plus some that Campbell thought were handy)

    def vertices(self):
        return list(self._vertices.values())

    def edges(self):
        return sorted(list(self._edges.values()))

    def num_vertices(self):
        return (len(self._vertices))

    def num_edges(self):
        return (len(self._edges))

    def incident(self, v):
        il = []
        for e in self.edges():
            if (v in e.ends()):
                il += [e]
        return (il)

    def in_incident(self, v):
        il = []
        for e in self.edges():
            if (v == e.head()):
                il += [e]
        return (il)

    def out_incident(self, v):
        il = []
        for e in self.edges():
            if (v == e.tail()):
                il += [e]
        return (il)

    def degree(self, v):
        return (len(self.incident(v)))

    def adjacent(self, v):
        av = []
        for i in self.edges():
            ie = i.ends()
            if (v in ie):
                if (ie[0] == v):
                    av += [ie[1]]
                else:
                    av += [ie[0]]
        return (av)

    def __repr__(self):
        rep = ""
        for edge in self._edges.values():
            rep += str(edge) + "\n"
        return rep


def parse_graph_file(file_path):
    graph = GraphEL()

    with open(file_path, 'r') as file:
        for edge_index, line in enumerate(file):
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue  # Skip invalid lines

            # Strip, and convert to numbers, if possible. The edge weight must be a number.
            for i in range(len(parts)):
                parts[i] = parts[i].strip()
                try:
                    parts[i] = int(parts[i])
                except Exception:   
                    try:
                        parts[i] = float(parts[i])
                    except Exception:
                        pass
            
            assert (isinstance(parts[0], int) or isinstance(parts[0], float))

            edge_weight, v1_name, v2_name = parts[0], parts[1], parts[2]
            vertex1 = graph._vertices.get(v1_name, VertexEL(v1_name))
            vertex2 = graph._vertices.get(v2_name, VertexEL(v2_name))
            
            graph.add_vertex(vertex1)
            graph.add_vertex(vertex2)
            
            edge = EdgeEL(edge_index, graph.get_vertex(v1_name), graph.get_vertex(v2_name))
            edge.set_value(edge_weight)
            
            graph.add_edge(edge)

    return graph
