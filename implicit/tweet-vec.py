import json

f = open(r'G:\twitter\Twitter\implicit\hash-dict-vec.json')
df = json.loads(f.read())
hashs = df['hashs']

g = open(r'G:\twitter\Twitter\tweet_hash.json')
dg = json.loads(g.read())

d = dict()
for u in dg:
    ll = dg[u]
    l = list()
    for h in hashs:
        if h in ll:
            l.append(1)
        else:
            l.append(0)
    d[u]= l

with open('tweet-vec.json','w') as jj:
    json.dump(d,jj)
