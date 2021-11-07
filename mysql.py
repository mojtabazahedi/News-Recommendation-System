import MySQLdb
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
db = MySQLdb.connect("localhost","root","","tweets" )
cur = db.cursor()
#####################################################
f = open("NewsData", "w")
cur.execute("SELECT * FROM tweets_sample WHERE content LIKE '%mashable%' ")
for row in cur.fetchall():
     rawtext = row[3]
     text = rawtext.encode('ascii', 'ignore')
     url = re.sub(r"http\S+", "", rawtext)
     out = "".join(c for c in url if c not in ('!','.',':','-','?','[',']','/','@'))
     f.write(out.lower())
     f.write("\n")

db.close()