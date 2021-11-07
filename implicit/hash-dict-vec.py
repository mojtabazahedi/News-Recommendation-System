import json


f = open(r'G:\twitter\Twitter\implicit\user-hash-plus-imp.json')
df = json.loads(f.read())

ll = list()

for t in df:
    ll.extend(df[t])

d = dict()
d['hashs']= list(set(ll))

print (len(list(set(ll))))
#with open('hash-dict-vec.json','w')as jj:
   # json.dump(d,jj)
