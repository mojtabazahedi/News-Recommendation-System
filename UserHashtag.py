__author__ = 'mojtaba'
import sqlite3
import re
##################
db = sqlite3.connect('TwitterData1')
c = db.cursor()
#######################
c.execute("select * from tweets WHERE text LIKE '%#%'")
for row in c.fetchall():
    rawtext = row[2]
    id=str(row[3])
    text = rawtext.encode('ascii', 'ignore')
    h=re.findall(r"#(\w+)", text)
    c.execute('''INSERT INTO hashtag (ID,Hashtag) VALUES(?,?)''', (id ,str(h)))
db.commit()
