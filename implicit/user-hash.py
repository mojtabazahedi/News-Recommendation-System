import json
import ast

f = open(r'G:\twitter\Twitter\tweet-hash')
d = dict()
for line in f:
    sentence=ast.literal_eval(line)
    d[sentence[0]] = sentence[1]

with open('user-hash.json','w')as jj:
    json.dump(d,jj)