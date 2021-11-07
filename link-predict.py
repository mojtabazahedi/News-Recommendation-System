import networkx as nx
import json
from networkx.readwrite.json_graph.node_link import node_link_graph
from networkx.algorithms.link_prediction import jaccard_coefficient
#########
f = open(r'G:\twitter\Twitter\graph\graph.json')
df=json.loads(f.read())

G=node_link_graph(df,multigraph=False)
u='346916581'
fff=jaccard_coefficient(G, [(u, '273003'),(u, '326934'),(u, '15029'),(u, '57565'),(u, '10085'),(u, '129604'),(u, '129585'),(u, '129594'),(u, '129608'),(u, '252129')])
e=list(fff)
print (e)