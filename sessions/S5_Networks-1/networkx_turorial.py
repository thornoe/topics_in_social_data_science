# press alt+i to toggle function options
import networkx as nx

G = nx.Graph()  # create an empty graph with no nodes nor edges
G.clear()

### NODES
G.add_node(1)   # add a single node

G.add_nodes_from([2, 3])    # adding a list of nodes

H = nx.path_graph(5)   # iterable container of the nodes (0,1,2,3,4)
G.add_nodes_from(H)     # adding the nodes in H as nodes of G

G.add_node(H)           # adding the container H as a node in G

### EDGES
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple
G.add_edges_from([(1, 2), (1, 3)])  # list of edges

G.add_edges_from(H.edges)   # from container

# ebunch of edges: iterable container of edge-tuples, e.g.  a 2-tuple of nodes
# or a 3-tuple with 2 nodes followed by an edge attribute dictionary such as
G.add_edges_from( [(2, 3, {'weight': 3.1415})] )    # edge attribute dictionary

# Example
G.clear()
G.add_node('spam')
G.add_nodes_from('spam')
G.add_edges_from([('s','p'), ('p','a'), ('a','m')])

### Overview
G.number_of_nodes()
G.number_of_edges()
list(G.nodes)
list(G.edges)
list(G.adj['p'])    # or list(G.neighbors(1))
G.degree['p']         # the number of edges incident to 1

# Reporting edges and degree from a subset of all nodes using an 'nbunch'
G.edges(['s', 'p'])
G.degree(['s', 'p'])

# REMOVING
G.remove_edge('s','p')
G.remove_edges_from([('p','a'), ('a','m')])
list(G.edges)
G.remove_node('spam')
G.remove_nodes_from('spam')
list(G.nodes)

# Creating graph by defining edges only - different formats
G.clear()
G.add_edge(1,2)
J = nx.DiGraph(G)   # create a DiGraph using the connections from G
list(J.edges())
edgelist = [(0,1),(1,2),(2,3),(3,4)]
K = nx.Graph(edgelist)
list(K.edges())
list(K.nodes)

# Different datatypes
nx.relabel.convert_node_labels_to_integers(G)
