import json
import operator
import io

f = open(r'G:\twitter\Twitter\user_tweet.json')
df =json.loads(f.read())
user_tweet = df['user_tweet']

g = open(r'G:\twitter\Twitter\graph\nodes.json')
dg = json.loads(g.read())
nodes = dg['nodes']
#print(nodes)
d = dict()

fun = operator.itemgetter('id')
l = list()
for u,t in user_tweet:
    l.append(dict(source= map(fun,nodes).index(u),target=map(fun,nodes).index(t)))

d['links']=l
with open('link-ut.json','w')as jj:
    json.dump(d,jj)
