__author__ = 'Macroboy'
import re
import sqlite3
import json
from collections import defaultdict

########################################################
db = sqlite3.connect('NewsData.db')
c = db.cursor()
########################################################
c.execute('select * from news')
dd=defaultdict(list)
rows = c.fetchall()
for row in rows:
    rawtext = row[1]
    id=str(row[2])
    text = rawtext.encode('ascii', 'ignore')
    url = re.sub(r"http\S+", "", text)
    out = "".join(c for c in url if c not in ("!", ".", ":", ";", ",", "?", "'", "@", "$", "~", "^", "%", "&", "/","(",")"))
    dd[id].append(out.lower())
with open('news.json','w')as f:
    json.dump(dd,f)

db.commit()
