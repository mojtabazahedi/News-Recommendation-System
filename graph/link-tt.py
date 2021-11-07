import json
import operator
import io

f = open(r'G:\twitter\Twitter\graph\tweetlink.json')
df =json.loads(f.read())

g = open(r'G:\twitter\Twitter\graph\nodes.json')
dg = json.loads(g.read())
nodes = dg['nodes']
#print(nodes)
d = dict()

fun = operator.itemgetter('id')
l = list()
for t in df:
    #r=str(u).lstrip()
    for st in df[t]:
        #t=str(su).lstrip()
        l.append(dict(source= map(fun,nodes).index(t),target=map(fun,nodes).index(st)))


d['links']=l
with open('link-tt.json','w')as jj:
    json.dump(d,jj)
