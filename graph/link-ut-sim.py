import json
import operator
import io

f = open(r'G:\twitter\Twitter\user-tweet-similar.json')
df =json.loads(f.read())
#user_tweet = df['user_tweet']

g = open(r'G:\twitter\Twitter\graph\nodes.json')
dg = json.loads(g.read())
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
with open('link-ut-sim.json','w')as jj:
    json.dump(d,jj)
