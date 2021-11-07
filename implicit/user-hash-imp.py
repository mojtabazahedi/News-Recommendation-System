import json
#from collections import defaultdict
import sqlite3

db = sqlite3.connect('TwitterData1')
a_cursor = db.cursor()



f = open(r'G:\twitter\Twitter\implicit\user-hash.json')
df = json.loads(f.read())
dg = df.copy()

for u in dg:
    a_cursor.execute('SELECT id,enrich FROM implicit WHERE id={}'.format(u))
    row=a_cursor.fetchall()
    mrow = map(lambda  a:a[1],row)
    dg[u].extend(mrow)
db.close()
with open('user-hash.imp.json','w')as jj:
    json.dump(dg,jj)
