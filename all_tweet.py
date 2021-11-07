import json
import sqlite3
#########
l = list()
d = dict()
db = sqlite3.connect('TwitterData1')
c = db.cursor()
########################################################
c.execute('select * from Goldset')
rows = c.fetchall()
for row in rows:
    l.append(str(row[2]))
d['tweet']= list(set(l))
with open('ttweet.json','w')as jj:
    json.dump(d,jj)

