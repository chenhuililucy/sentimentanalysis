

#In this piece of code, I want to figure out what is th m.start():-20 line is doing
#In the context of onlinecodes.py
#I figured that it is extracting the 20 characters before the occurence of m.start

import os
import re 

filecontent=[]


root="/Users/lucy/Desktop/summer/SummaryDataFile/American Standard"
with open(os.path.join(root,"836102-2008.txt" ), "r") as auto:
    for line in auto: 
        filecontent.append(line)
        filecontent1= ''.join(filecontent)
        lstr1=filecontent1.lower()
for m in re.finditer("item 7",lstr1):
    if not m:
        break
    else:
        substr1=lstr1[m.start()-50:m.start()]
        print(m.start())
        print(substr1)
         
         
    


