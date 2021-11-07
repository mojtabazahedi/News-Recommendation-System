import json
import operator
import io
import yaml

f = open(r'G:\twitter\Twitter\graph\links.json')
df = yaml.safe_load(f.read())

g = open(r'G:\twitter\Twitter\graph\nodes.json')
dg = yaml.safe_load(g.read())
nodes = dg['nodes']
#print(nodes)
d = dict()

fun = operator.itemgetter('id')
l = list()
for u in df:
    #r=str(u).lstrip()
    for su in df[u]:
        #t=str(su).lstrip()
        l.append(dict(source= map(fun,nodes).index(u),target=map(fun,nodes).index(su)))


d['links']=l
with open('link-uu.json','w')as jj:
    json.dump(d,jj)
