import networkx as nx
import matplotlib.pyplot as plt

class GraphVisualizer:

    def visualize(self, world_state):

        G = nx.DiGraph()

        # nodos = procesos
        for p in world_state["processes"]:
            G.add_node(p["process"])

        # relaciones = edges
        for r in world_state["relations"]:
            G.add_edge(r["from"], r["to"], label=r["type"])

        pos = nx.spring_layout(G)

        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue")
        
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.title("AWGS World Graph")
        plt.show()
