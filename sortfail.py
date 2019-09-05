import os
import csv


#os.mkdir("/Users/lucy/Desktop/fail/"+"fail.csv")
os.chdir("/Users/lucy/Desktop/fail")
for f in os.listdir(): 
    name, ext = os.path.splitext(f)
    fn = name.split('-')
    print(fn[0]+'|')
    with open('hello.csv', 'w', newline='') as infile:
        #writer = csv.writer('lol.csv', delimiter=',', quotechar='|')
        #writer = csv.writer('hello.csv', delimiter=',')
        #for row in writer:
        #for row in infile: 
        #for item in fn[0]:
        infile.write(fn[0]+'\n')
        #infile.write('\n')

            #for r in csvr:
            #infile.write(fn[0])


infile.close()
            
