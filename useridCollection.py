__author__ = 'Macroboy'
id_data = []
textfile = open('bbctech.txt', "r")
id_data = textfile.read().split(',')
####################################

for uid in id_data:
    sourcetarget =open('useridCollection').read()
    if uid not in sourcetarget:
        target = open('useridCollection','a')
        target.write(uid)
        target.close()




