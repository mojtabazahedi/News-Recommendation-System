import json
from collections import defaultdict
import io

f= io.open(r'G:\twitter\Twitter\tweet_hash.json',encoding='utf-8')
df = json.loads(f.read())
th = df['tweet_hash']

d= defaultdict(list)

for i in th:
    d[str(i[0])].append(str(i[1]))

with io.open('tweet_hash_list.json','w',encoding='utf-8')as jj:
    json.dump(d,jj)
