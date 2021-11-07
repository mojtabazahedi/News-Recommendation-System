__author__ = 'Macroboy'
import re
import sqlite3
import ast


########################################################
db = sqlite3.connect('TwitterData1')
c = db.cursor()
########################################################
f=open("usertweet","w")
I=open("UserID","r")
for line in I:
    sentence=ast.literal_eval(line)
    c.execute('SELECT * FROM tweets WHERE userid=?',[sentence])
    rows = c.fetchall()
    for row in rows:
            rawtext = row[2]
            text = rawtext.encode('ascii', 'ignore')
            url = re.sub(r"http\S+", "", text)
            out = "".join(c for c in url if c not in ("!", ".", ":", ";", ",", "?", "'", "@", "$", "~", "^", "%", "&", "/","(",")"))+"."
            tweets="".join(out.lower())
    f.write(str(sentence)+','+tweets+'\n')
db.commit()
