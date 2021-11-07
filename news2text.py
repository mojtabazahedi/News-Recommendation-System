import ast
import json
from collections import defaultdict
t=open('NewsData','w')
f = open('news.json')
data = json.loads(f.read())
for key in data:
    t.write('['+"'"+key+"'"+']'+','+ str(data[key])+'\n')