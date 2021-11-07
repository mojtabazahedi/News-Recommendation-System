import ast
import json
from collections import defaultdict
t=open('tweets','w')
f = open('tweets.json')
data = json.loads(f.read())
for key in data:
    t.write('['+"'"+key+"'"+']'+','+ str(data[key])+'\n')