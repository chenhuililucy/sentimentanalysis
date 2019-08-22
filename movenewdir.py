#I don't know why this piece of codes doesnt do anything; it should. 

import re, os
import glob
import shutil

#the glob module matches all files that are of the following forms 
# import glob
# glob.glob('./[0-9].*')
#['./1.gif', './2.txt']
# glob.glob('*.gif')
#['1.gif', 'card.gif']
# glob.glob('?.gif')
#['1.gif']

year='2000' #cant pass year in as an integer

os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1995-2000'+'/'+year+'/QTR1')

for f in os.listdir(): 
    filename, filetype = os.path.splitext(f)
        #yearform="-"+year
    if filename.endswith(year):
        shutil.move(f, '/Users/lucy/Desktop/allfiles')



os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1995-2000'+'/'+year+'/QTR2')

for f in os.listdir(): 
    filename, filetype = os.path.splitext(f)
        #yearform="-"+year
    if filename.endswith(year):
        shutil.move(f, '/Users/lucy/Desktop/allfiles')




os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1995-2000'+'/'+year+'/QTR3')

for f in os.listdir(): 
    filename, filetype = os.path.splitext(f)
        #yearform="-"+year
    if filename.endswith(year):
        shutil.move(f, '/Users/lucy/Desktop/allfiles')




os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1995-2000'+'/'+year+'/QTR4')

for f in os.listdir(): 
    filename, filetype = os.path.splitext(f)
        #yearform="-"+year
    if filename.endswith(year):
        shutil.move(f, '/Users/lucy/Desktop/allfiles')


#you also cant replace os.chdir by dir because in that way the computer recognizes it as a string