import json
from collections import defaultdict
f = open(r'G:\twitter\Twitter\user-tweet.json')
df = json.loads(f.read())

g = open(r'G:\twitter\Twitter\implicit\user-hash.imp.json')
dg = json.loads(g.read())

d = defaultdict(list)
for u in df:
    for t in df[u]:
        try:
            d[u].extend(list(set(dg[t])))
        except:
            continue
sd = dict()
for i in d:
    sd[i] = list(set(d[i]))

with open('user-hash-plus-imp.json','w') as jj:
    json.dump(sd, jj)