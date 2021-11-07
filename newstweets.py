__author__ = 'Macroboy'
import re
import sqlite3

########################################################
db = sqlite3.connect('NewsData.db')
c = db.cursor()
########################################################
c.execute('select * from news')
rows = c.fetchall()
for row in rows:
    rawtext = row[1]
    id=str(row[2])
    text = rawtext.encode('ascii', 'ignore')
    url = re.sub(r"http\S+", "", text)
    c.execute('''INSERT INTO textonly ( text,id) VALUES(?,?)''', (url ,id))
    #print rawtext,
    #report = c.execute("UPDATE tweets set text= ? WHERE ID= ?", (str(url), str(id)))
    #print c.rowcount
db.commit()




