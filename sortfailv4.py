import os
import csv


os.chdir("/Users/lucy/Desktop/fail")

with open('hello.csv', 'w', newline='') as infile:
#os.mkdir("/Users/lucy/Desktop/fail/"+"fail.csv")
    for f in os.listdir(): 
        name, ext = os.path.splitext(f)
        fn = name.split('-')
        print('| cik'+'=='+fn[0]+' ///')
 
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
            
