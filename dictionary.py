#This piece of code will output weights of documents in the form of a matrix. 

#You need to have two csv files that store words we are looking for in the dictionary 
#As with the termination of the second for loop, the csv file automatically closes, the first for loop would not run
#The only way to do this is to store the dictionary as several dictionaries each with 1 column
  


import os
import csv

os.chdir("/Users/lucy/Desktop/builddic")
#change directory to location of the csv files where you read in the dictaionry 




posperflist=[]

with open("postperf.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:


        ###############

        #Syntax error: do not make this error again! 
        # with row as r: 
        #for row[0] in row: 

        ###############


        posperf=row[0]


         ###############
        #print(posperf)
            #print(row[0])
            # posperf is a string, not a list, no need to say  
            #for item in posperf:
                #print(item)
         ###############


        
        with open("amplifier","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()

                
        #new=[posperf].append(amplifier) 


                new=posperf+" "+amplifier
                new2=amplifier+" "+posperf


                ######
                #print(new)
                #print(new2)
                #####
                
                posperflist.append(new)
                posperflist.append(new2)
                print(perflist)

    
with open("Book1.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:


        ###############

        #Syntax error: do not make this error again! 
        # with row as r: 
        #for row[0] in row: 

        ###############


        posperf=row[0]


         ###############
        #print(posperf)
            #print(row[0])
            # posperf is a string, not a list, no need to say  
            #for item in posperf:
                #print(item)
         ###############


        
        with open("Book2.csv","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()

                
        #new=[posperf].append(amplifier) 


                new=posperf+" "+amplifier
                new2=amplifier+" "+posperf


                ######
                #print(new)
                #print(new2)
                #####
                
                posperflist.append(new)
                posperflist.append(new2)
                print(perflist)

    




negperflist=[]

with open("posperf.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:


        ###############

        #Syntax error: do not make this error again! 
        # with row as r: 
        #for row[0] in row: 

        ###############


        posperf=row[0]


         ###############
        #print(posperf)
            #print(row[0])
            # posperf is a string, not a list, no need to say  
            #for item in posperf:
                #print(item)
         ###############


        
        with open("amplifier.csv","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()

                
        #new=[posperf].append(amplifier) 


                new=posperf+" "+amplifier
                new2=amplifier+" "+posperf


                ######
                #print(new)
                #print(new2)
                #####
                
                perflist.append(new)
                perflist.append(new2)
                print(perflist)

    


intlist=[]

with open("Book1.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:


        ###############

        #Syntax error: do not make this error again! 
        # with row as r: 
        #for row[0] in row: 

        ###############


        posperf=row[0]


         ###############
        #print(posperf)
            #print(row[0])
            # posperf is a string, not a list, no need to say  
            #for item in posperf:
                #print(item)
         ###############


        
        with open("Book2.csv","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()

                
        #new=[posperf].append(amplifier) 


                new=posperf+" "+amplifier
                new2=amplifier+" "+posperf


                ######
                #print(new)
                #print(new2)
                #####
                
                perflist.append(new)
                perflist.append(new2)
                print(perflist)






with open 