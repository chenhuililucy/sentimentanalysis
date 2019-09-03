import os
os.chdir('/Users/lucy/Desktop/summer/datacollection/10-X_C_1993-2000/1995/QTR3')
for f in os.listdir():
    filename, filetype = os.path.splitext(f)
    fn = filename.split('-')
    filename = '-'.join([fn[0], fn[1]])
    file1=filename+".txt"
    os. rename(f, file1)