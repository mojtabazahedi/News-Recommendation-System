import json
import yaml

f = open(r'G:\twitter\Twitter\uusers.json')
df = json.loads(f.read())
users = df['users']

g = open(r'G:\twitter\Twitter\alltweet.json')
dg = json.loads(g.read())
tweet = dg['tweet']
dd = dict()
l = list()

for i in users:
    l.append(dict(id=i))

for j in tweet:
    l.append(dict(id=j))

dd['nodes']=l
with open('nodes.json','w')as jj:
    json.dump(dd,jj)

