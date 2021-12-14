from day12data import test_data_10
import networkx as nx

data = test_data_10
graph = nx.Graph(data)

for item in nx.bfs_edges(graph, "start"):
    print(item)
    if item[0] != "start" and item[-1] != "end":
        continue


