from Graph import Graph
import math
from min_edge_cover import get_min_edge_cover, get_min_graph, probabilistic_search
import matplotlib.pyplot as plt

n_vertices = 6

max_n_edges = int(math.factorial(n_vertices)/(math.factorial(n_vertices-2)*2))
#n_edges = 6

graph = Graph(random=True, n=n_vertices, m=max_n_edges)

full_fig = graph.show_graph(filename="full_graph.png")

for v in graph.get_graph().values():
    assert len(v) > 0, "Isolated vertices, no edge cover possible"

#method = "exhaustive"
method = "probabilistic"    

#min_edge_cover, min_edges = get_min_edge_cover(graph, method=method)

#probabilistic_search(graph)

min_graph = get_min_graph(graph, method=method)

min_fig = min_graph.show_graph(filename="min_graph.png", minimum=True)

#average, variance = probabilistic_results(graph)
#std = variance/10
#print("Most likely result is %f +- %f" % (average, std))

plt.show()