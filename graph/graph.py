import json

f1 = open(r'G:\twitter\Twitter\graph\link-uu.json')
df1 = json.loads(f1.read())
links = df1['links']

f2 = open(r'G:\twitter\Twitter\graph\link-ut.json')
df2 = json.loads(f2.read())
links.extend(df2['links'])

f3 = open(r'G:\twitter\Twitter\graph\link-tt.json')
df3 = json.loads(f3.read())
links.extend(df3['links'])

f4=open(r'G:\twitter\Twitter\graph\link-ut-sim.json')
df4=json.loads(f4.read())
links.extend(df4['links'])

g = open(r'G:\twitter\Twitter\graph\nodes.json')
dg = json.loads(g.read())
nodes = dg['nodes']

d = dict()
d['nodes']=nodes
d['links']=links

with open('graph.json','w')as gg:
    json.dump(d,gg)
