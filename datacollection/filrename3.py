import os
import bs4 

os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1993-2000/1995/QTR2/need\ sort ')
for f in os.listdir():
        fn = filename.split('-')
        filename = '-'.join([fn[0], fn[1]])
        file1=filename+".txt"
        os. rename(f, file1)
