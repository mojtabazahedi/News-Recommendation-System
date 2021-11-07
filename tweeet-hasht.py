import sqlite3
import re

db = sqlite3.connect('TwitterData1')
c = db.cursor()

f = open('tweet-hash', "w")

c.execute('select * from hashtag')
rows = c.fetchall()
for row in rows:
    hashtag = row[1]
    id=str(row[0])
    f.write(id+','+str(hashtag)+'\n')