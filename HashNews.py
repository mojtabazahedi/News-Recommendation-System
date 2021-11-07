import sqlite3
import ast
db_a = sqlite3.connect('TwitterData1')
db_b = sqlite3.connect('TwitterData1')
############################################
b_cursor=db_b.cursor()
########
a_cursor = db_a.cursor()
a_cursor.execute('SELECT * FROM implicit')
hashtags=a_cursor.fetchall()
###################

for sentences in hashtags:
    tweetlist=[]
    enrich=tuple(sentences)[1]
    Enrich=tuple(sentences)[1].title()
    b_cursor.execute("SELECT * FROM Goldset WHERE text LIKE '%#"+enrich+"%' OR text lIKE '%#"+Enrich+"%' ")
    result=b_cursor.fetchall()
    if len(result) !=0:
        for tweet in result:
            tweetlist.append(tweet[2])
        a_cursor.execute('UPDATE implicit SET newsid=? WHERE id=? and enrich=?',(str(tweetlist),sentences[0],enrich))
        db_a.commit()



