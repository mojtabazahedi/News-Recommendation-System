__author__ = 'mojtaba'
import sqlite3
import re
import ast
#################
db = sqlite3.connect('TwitterData1')
c = db.cursor()
########################################################
#I=open("Uid","r")
#for line in I:
    #sentence=ast.literal_eval(line)
    #uid=sentence
c.execute("SELECT * FROM tweets WHERE userid like'%931826418%'")
rows = c.fetchall()
for row in rows:
        uid=str(row[0])
        rawtext = row[2]
        id=str(row[3])
        c.execute('''INSERT INTO Goldset (Tid,Text,Uid) VALUES(?,?,?)''', (id ,rawtext,uid))
db.commit()