#I can do .lower() for all files and this would get rid of all the weird uppercase, 
#I can do re.match and re.sub to get rid of all '-' in the document
# and the first I can use ‘exhibit 13’ as a start match and ‘exhibit 21’ as an end match 
# equity part is common stockholders' equity or stock market information

debug=True
import re 
import os


#directory to save file if item is found
item13_dir="/Users/lucy/Desktop/assortedcodes/assortedcodes/sortfailed/real"

def parse_mda(text,start=0):
    mda=""
    end = 0

    item13_begins = ['exhibit 13','ex 13',"ex13"]
    item13_ends = ["common stockholder's equity", "stock market information"]
    text1=text.lower()
    text11 = re.sub(r'-', ' ', text1)
    text12 = re.sub(r'\d', '', text11 )
    text13 = re.sub(r'=', '', text12 )
    text2 = re.sub(r'$', '', text13 )

    text2 = text2[start:]
    a={}
    for item13 in item13_begins:
        if not item13: 
            print("item13 not found")
            break 
        else: 
            begin = text2.find(item13)
        if begin != -1:
            print(item13)
            break
    
    if begin != -1:  # Begin found
        for item13ends in item13_ends:
            end = text1.find(item13ends, begin + 1)
            if debug:
                print()
            if end != -1:
                break

            
        if end > begin:
            #if len[begin:end]>20
            mda = text1[begin:end].strip()
            if end !=-1: 
                 mda = text1[begin:].strip()
                 print("exception")
        else:
            end = 0
    
    return mda, end


#original directory
file1=[]
for root, dirs, files in os.walk("/Users/lucy/Desktop/assortedcodes/assortedcodes/sortfailed/item13_failed"):
    for file in files:
        if '.txt' in file:
           
            #files.append(os.path.join(root,file))
            with open(os.path.join(root, file), "r") as auto:
                text = auto.read()
                text1=text.lower()
                text11 = re.sub(r'-', ' ', text1)
                text12 = re.sub(r'\d', '', text11 )
                text13 = re.sub(r'=', '', text12 )
                text2 = re.sub(r'$', '', text13 )
                print(file)
                #print(text1) 
                # test if text.lower() is working 
                

              
      
                # Find MDA section
                item13found, end = parse_mda(text2)
                # Parse second time if first parse results in index

                if item13found:
                    filename = os.path.basename(os.path.join(root, file))
                    name, ext = os.path.splitext(file)
                    item13_path = os.path.join(item13_dir, name + "item13"+".txt")
                    print("writing item13 to {}".format(item13_path))
                    #The usage of function above is print ("Hello, I am {} years old !".format(18))  
                    #>>>Hello, I am  18 years old!
                    with open(item13_path, 'w') as fout:
                        fout.write(item13found)
                else:
                    print("extract item13 failed - {}".format(file))
                    #directory to save file if extraction failed 
                    with open("/Users/lucy/Desktop/assortedcodes/assortedcodes/sortfailed/item131failed/"+file, "w") as f: 
                        f.write(text2)





