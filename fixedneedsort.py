
import os
os.chdir("/Users/lucy/Desktop/needsort")

for f in os.listdir(): 
    newfilename=f+'.txt'
    filecontent=[]
    for line in f: 
        filecontent.append(line)
        #filecontent1=filecontent.split()
        filecontent1=''.join(filecontent)
        with open(newfilename,"w") as file: 
            file.write(filecontent1)
            file.close()
