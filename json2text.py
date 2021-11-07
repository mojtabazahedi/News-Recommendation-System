import ast
import json
from collections import defaultdict
t=open('gold','w')
f = open('gold.json')
data = json.loads(f.read())
for key in data:
    t.write('['+"'"+key+"'"+']'+','+ str(data[key])+'\n')