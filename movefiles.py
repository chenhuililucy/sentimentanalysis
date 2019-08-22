import csv 
import os 
import shutil
import json 
import adict

os.chdir('/Users/lucy/Desktop/summer/datacollection/usedcsv')


with open('14-40.csv', 'r') as f:
    reader=csv.reader(f)
    os.chdir('/Users/lucy/Desktop/summer/Summarydatafile')
    for row in reader:
        os.makedirs(row[0], exist_ok=True) #This is for the newest version of python, for older versions, use the codes below 
    #for row in reader: 
        #os.mkdir(row[0])
        #while True:
            #row[0] = next_dir_name()
            #try:
                #os.makedirs(row[0])
                #break
            #except OSError, e:
                #if e.errno != os.errno.EEXIST:
                    #raise   
        # time.sleep might help here
                #pass

os.chdir('/Users/lucy/Desktop/summer/datacollection/usedcsv')

with open('14-40.csv', 'r') as f:
    os.chdir('/Users/lucy/Desktop/10-K405')
    reader=csv.reader(f)
    company={}
    for row in reader: 
        company[row[0]]={'cik':row[1]}
        for f in os.listdir(): 
            filename, filetype = os.path.splitext(f)
            fn = filename.split('-')
            if row[1]==fn[0]: 
                newdir='/Users/lucy/Desktop/summer/Summarydatafile/'+row[0]
                shutil.move(f,newdir)
                #shutil.move(os.path.join('/Users/lucy/Desktop/summer/datacollection/10-X_C_1993-2000/1996/QTR1', row[1]), os.path.join('/Users/lucy/Desktop/summer/Summarydatafile/', row[0]))

os.chdir('/Users/lucy/Desktop/summer/datacollection/usedcsv')


    #Originally with this piece of code I wrote I ran into errors as i acccidentally appended company to original directory
    #Actually what I should have done was to append row[0]
    #On this occasion I got interested in seeing how to rearrange dictionaries into string
    #which was the json.dumps(dict) command 

    # Can also be done through pickle 
    # Save a dictionary into a pickle file.
    #import pickle
    #favorite_color = { "lion": "yellow", "kitty": "red" }
    # pickle.dump( favorite_color, open( "save.p", "wb" ) )

with open('14-40.csv', 'r') as f:
    os.chdir('/Users/lucy/Desktop/10-K-A')
    reader=csv.reader(f)
    company={}
    for row in reader: 
        company[row[0]]={'cik':row[1]}
        for f in os.listdir(): 
            filename, filetype = os.path.splitext(f)
            fn = filename.split('-')
            if row[1]==fn[0]: 
                newdir='/Users/lucy/Desktop/summer/Summarydatafile/'+row[0]
                shutil.move(f,newdir)
                #shutil.move(os.path.join('/Users/lucy/Desktop/summer/datacollection/10-X_C_1993-2000/1996/QTR1', row[1]), os.path.join('/Users/lucy/Desktop/summer/Summarydatafile/', row[0]))

os.chdir('/Users/lucy/Desktop/summer/datacollection/usedcsv')

with open('14-40.csv', 'r') as f:
    os.chdir('/Users/lucy/Desktop/allfiles')
    reader=csv.reader(f)
    company={}
    for row in reader: 
        company[row[0]]={'cik':row[1]}
        for f in os.listdir(): 
            filename, filetype = os.path.splitext(f)
            fn = filename.split('-')
            if row[1]==fn[0]: 
                newdir='/Users/lucy/Desktop/summer/Summarydatafile/'+row[0]
                shutil.move(f,newdir)
                #shutil.move(os.path.join('/Users/lucy/Desktop/summer/datacollection/10-X_C_1993-2000/1996/QTR1', row[1]), os.path.join('/Users/lucy/Desktop/summer/Summarydatafile/', row[0]))

os.chdir('/Users/lucy/Desktop/summer/datacollection/usedcsv')
