from pyvis.network import Network
import numpy as np

def build_graph_vizualization(flight_list, flight_pairs):
    graph = Network(height="500px", width="800px", notebook=False)

    # Add nodes to the graph
    for flight in flight_list:
        graph.add_node(flight, label=flight)

    # Add edges to the graph
    for pair in flight_pairs:
        graph.add_edge(pair[0], pair[1])

    # Save the graph to an HTML file or display it in a Jupyter Notebook
    graph.write_html('plots/graph_vizualization.html')