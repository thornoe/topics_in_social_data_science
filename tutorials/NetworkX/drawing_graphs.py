# press alt+i to toggle function options
import networkx as nx
import matplotlib.pyplot as plt

def opt(color):
    options = {
        'with_labels': True,
        'font_weight': 'bold',
        'node_color': color,
        'node_size': 300,
        'width': 1,
    }
    return options

# Example graph
    edgelist = [(0,1),(1,2),(2,3),(3,4)]
    G = nx.Graph(edgelist)
    G.add_edge(1, 3)
    list(G.edges())
    plt.clf()
    plt.subplot(121)
    nx.draw(G, **opt('r'))
    plt.subplot(122)
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], **opt('b'))
    plt.show()

# Petersen Graph
    plt.clf()
    G = nx.petersen_graph()
    plt.subplot(121)    # left panel
    nx.draw(G, **opt('g'))
    plt.subplot(122, facecolor='y')    # right panel
    nx.draw_shell(G, nlist=[range(5, 10), range(5)], **opt('y'))
    plt.savefig("sessions/S5_Networks_1/Petersen.png")
    plt.show()
