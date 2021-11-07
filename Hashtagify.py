import requests
import json
import re
import ast
import sqlite3
db = sqlite3.connect('TwitterData1')
c = db.cursor()

##########################################################
f = open("hash", "r")
##########################################################
for line in f:
    #y=line.split(',')
    sentence=ast.literal_eval(line)
    id=sentence[0]
    hashtag = sentence[1]
    hashtaglist=[]
    for x in list(hashtag):
    #print(hashtag)
        url = "https://api.hashtagify.me/1.0/tag/"+str(x).lower()
        headers = {
        'authorization': "Bearer 2e5b41d596ffb4eecb8d7214db0f50707ea4ff2e",
        'cache-control': "no-cache"
                    }
        response = requests.request("GET", url, headers=headers).json()
        for tag in response:
                hashtaglist.append(tag)
                #print(hashtaglist)
                c.execute('INSERT into implicit VALUES (?,?,?)',(id,tag,None))
    db.commit()

