import json
import sqlite3
from collections import defaultdict

#########
l = list()
d = dict()
db = sqlite3.connect('TwitterData1')
c = db.cursor()
########################################################
c.execute('select * from implicit')
rows = c.fetchall()
dd = defaultdict(list)
for row in rows:
    dd[str(row[0]).lstrip()].append(row[1])
    #l.append((str(row[0]).lstrip(),row[1]))
#d['tweet_hash']= list((l))
with open('tweet_hash.json','w')as jj:
    json.dump(dd,jj)
