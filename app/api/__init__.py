from app.components.graph import build_graph
from app.components.ner import *
from app.components.classify import * 

graph, nodes, edges = build_graph('app/components/config_graph.json')
