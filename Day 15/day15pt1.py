from day15data import test_data, data
import networkx as nx
import numpy as np

#data = test_data

graph = nx.grid_2d_graph(len(data), len(data[0]))

nodes = list(graph.nodes())
start = nodes[0]
end = nodes[-1]

def node_weight(u, v, d):
    return data[v[0]][v[1]]

route = nx.dijkstra_path(graph, source=start, target=end, weight=node_weight)
risk = 0
for step in route[1:]:
    risk += data[step[0]][step[1]]
    
print(risk)