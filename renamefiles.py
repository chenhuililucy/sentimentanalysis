import os

#drag directory into the terminal and copy the directory to the python page
os.chdir('/Users/lucy/Desktop/10-K-A')


#this code gives us a tuple, and each element gives us a file name without the extension and the next part with the extension
#for f in os.listdir():
 # filename, filetype = os.path.splitext(f)
 # filename.split('_') = year,formtype,edgar,data,cik,no,last
#    print ('{}-{}'.format(cik,year))

#for f in os.listdir():
       # ar=os.listdir()
        #filename, filetype = os.path.splitext(f)
        #fn = filename.split('_')
        #if fn[1] == "10-K":
               # yearmonth= fn[0]
               # year=yearmonth[:4]
               # filename = '-'.join([fn[4], year])
               # text=f.get_text()
               # f = open(saveasnew, "w+")
                #f.write(text)
                #f.close()


#for f in os.listdir():
        #filename, filetype = os.path.splitext(f)
        #fn = filename.split('_')
        #if fn[1] == "10-K-A": 
                #yearmonth= fn[0]
                #year=yearmonth[:4]
                #filename = '-'.join([fn[4], year])
                #file1=filename+".txt"
                #os. rename(f, file1)

for f in os.listdir(): 
        filename, filetype = os.path.splitext(f)
        file1=filename+"-A.txt"
        os.rename (f, file1)


