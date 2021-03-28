import json


def build_graph(path):
    f = open(path, 'r')
    json_graph = json.load(f)
    nodes = json_graph['nodes']
    edges = json_graph['edges']
    config = json_graph['config']

    graph = dict()
    keys = config.keys()
    for node in keys:
        if node not in graph:
            graph[node] = dict()
            for edge in config[node]:
                value = config[node][edge]
                graph[node][edge] = value
                
    return graph, nodes, edges 
    

