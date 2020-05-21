"""

import wrds
db = wrds.Connection()
libraries = db.list_libraries()
print(libraries)

"""
import glob

#extract ciks of all filings

s=set()


corpus="/Users/lucy/Desktop/others/newdictestn/newdic/*.txt"
direct="/Users/lucy/Desktop/assortedcodes/fin.txt"

for files in glob.glob(corpus):
    st=""
    for e in str(files): 
        #print(e)
        if e.isalpha() or e=="/": 
            continue
        elif e !="-": 
            st+=e
        elif e=="-": 
            break
    if st not in s:
        s.add(st)

print(s)  
fsent=open(direct,"w")
for e in s: 
    fsent.write(e)
    fsent.write("\n")
fsent.close()
