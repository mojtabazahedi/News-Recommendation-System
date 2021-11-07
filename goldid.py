__author__ = 'mojtaba'
import sqlite3
import ast
#################
db = sqlite3.connect('TwitterData1')
c = db.cursor()
##################
f=open('Uid','w')
c.execute('select * from tweets group by userid having count(text)>400')
rows = c.fetchall()
for row in rows:
    id=row[0]
    #sentence=ast.literal_eval(id)
    f.write(id)
