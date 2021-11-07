import requests
import json
import re
import sqlite3
########################################################
db = sqlite3.connect('TwitterData')
c = db.cursor()
url = 'http://tagme.di.unipi.it/tag'
########################################################
c.execute('select * from tweets')
rows = c.fetchall()
for row in rows:
    rawtext = row[2]
    keyID = str(row[3])
    text = rawtext.encode('ascii', 'ignore')
    response = requests.post(url, data={"key": "419FEqLpCr69000", "epsilon": "0.35", "tweet": "True", "text": rawtext, "lang": "en", "include_abstract": "true", "include_categories": "true"}).json()
    report = c.execute('''INSERT INTO Tagme(id, json) VALUES(?,?)''', (keyID, str(response)))
    print c.rowcount
    db.commit()






