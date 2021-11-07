import json
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
f = open(r'G:\twitter\Twitter\implicit\user-vec.json')
df = json.loads(f.read())

g = open(r'G:\twitter\Twitter\implicit\tweet-vec.json')
dg = json.loads(g.read())

def gen(u):
    for t in dg:
       yield (t , cosine_similarity(np.array(df[u]).reshape(1, -1), np.array(dg[t]).reshape(1, -1)))




x = gen("2239281649")
print(next(x))
print(next(x))



