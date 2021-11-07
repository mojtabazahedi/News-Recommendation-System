import sqlite3
import re
####################
db = sqlite3.connect('TwitterData1')
c = db.cursor()
###################
f = open("hash", "w")
c.execute('select * from hashtag')
rows = c.fetchall()
for row in rows:
    Hashtag = row[1]
    ID = str(row[0])
    text = Hashtag.encode('ascii', 'ignore')
    f.write(ID+','+text+'\n')
f.close()
