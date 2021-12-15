from day15data import test_data, data
import networkx as nx

# data = test_data

shape = len(data)
graph = nx.grid_2d_graph(shape*5, shape*5)

start = (0, 0)
end = (shape*5-1, shape*5-1)

def get_node_weight(v):
    x_tile, x_item = divmod(v[0], shape)
    y_tile, y_item = divmod(v[1], shape)
    data_val = data[x_item][y_item] - 1
    val = (data_val + x_tile + y_tile) % 9
    return val + 1

def node_weight(u, v, d):
    return get_node_weight(v)

route = nx.dijkstra_path(graph, source=start, target=end, weight=node_weight)

risk = sum([get_node_weight(step) for step in route[1:]])
    
print(risk)
