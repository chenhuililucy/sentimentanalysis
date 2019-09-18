
# -*- coding: utf-8 -*-
import re
import os

#os.mkdir("/Users/lucy/Desktop/fail/")
mda_dir="/Users/lucy/Desktop/dictionary/"

def parse_mda(text, start=0):
    debug = False
    """Parse normalized text 
    """

    mda = ""
    end = 0
    """
        Parsing Rules
    """

    # Define start & end signal for parsing
    #backward slash n => line return, carriage return, (dont need backslash n?) check what backward slash n mean, anything having backward slash n is not gonna do anything 
    #need Item 7./n will pick up more 
    item7_begins = [
        'item 7.', 'item 7 –', 'item 7:', 'item 7 ', 'item 7\n', 'item 7'
        "item 7. management's discussion and analysis",
        "item 7.management's discussion and analysis",
        "item7. management's discussion and analysis",
        "item7.management's discussion and analysis",
        "item 7. management discussion and analysis",
        "item 7.management discussion and analysis",
        "item7. management discussion and analysis",
        "item7.management discussion and analysis",
        "item 7 management's discussion and analysis",
        "item 7management's discussion and analysis",
        "item7 management's discussion and analysis",
        "item7management's discussion and analysis",
        "item 7 management discussion and analysis",
        "item 7management discussion and analysis",
        "item7 management discussion and analysis",
        "item7management discussion and analysis",
        "item 7: management's discussion and analysis",
        "item 7.MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS"
        "item7: management's discussion and analysis", "item7:management's discussion and analysis","item 7: management discussion and analysis","item 7:management discussion and analysis",
        "item7: management discussion and analysis","item7:management discussion and analysis"
        "\nitem 7\. managements discussion and analysis","\nitem 7\.managements discussion and analysis","\nitem7\. managements discussion and analysis","\nitem7\.managements discussion and analysis",
        "\nitem 7\. management discussion and analysis","\nitem 7\.management discussion and analysis","\nitem7\. management discussion and analysis","\nitem7\.management discussion and analysis",
        "\nitem 7 managements discussion and analysis","\nitem 7managements discussion and analysis","\nitem7 managements discussion and analysis","\nitem7managements discussion and analysis",
        "\nitem 7 management discussion and analysis","\nitem 7management discussion and analysis","\nitem7 management discussion and analysis","\nitem7management discussion and analysis","\nitem 7: managements discussion and analysis",
        "\nitem 7:managements discussion and analysis", "\nitem7: managements discussion and analysis", "\nitem7:managements discussion and analysis","\nitem 7: management discussion and analysis","\nitem 7:management discussion and analysis",
        "\nitem7: management discussion and analysis","\nitem7:management discussion and analysis","item 7.MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS"
        "management's discussion and analysis"
    ]
    item7_ends = ['item 7a']
    if start != 0:
        item7_ends.append('\nitem 7')  # Case: ITEM 7A does not exist
    item8_begins = ["item 8", 
        "item 8\. financial statements",
       "item 8\.financial statements",
        "item8\. financial statements",
        "item8\.financial statements",
        "item 8 financial statements",
        "item 8financial statements",
        "item8 financial statements",
        "item8financial statements",
        "item 8a\. financial statements",
        "item 8a\.financial statements",
        "item8a\. financial statements",
        "item8a\.financial statements",
        "item 8a financial statements",
        "item 8afinancial statements",
        "item8a financial statements",
        "item8afinancial statements",
        "item 8\. consolidated financial statements",
        "item 8\.consolidated financial statements",
        "item8\. consolidated financial statements",
        "item8\.consolidated financial statements",
        "item 8 consolidated  financial statements",
        "item 8consolidated financial statements",
        "item8 consolidated  financial statements",
        "item8consolidated financial statements",
        "item 8a\. consolidated financial statements",
        "item 8a\.consolidated financial statements",
        "item8a\. consolidated financial statements",
        "item8a\.consolidated financial statements",
        "item 8a consolidated financial statements",
        "item 8aconsolidated financial statements",
        "item8a consolidated financial statements",
        "item8aconsolidated financial statements",
        "item 8\. audited financial statements",
        "item 8\.audited financial statements",
        "item8\. audited financial statements",
        "item8\.audited financial statements",
        "item 8 audited financial statements",
        "item 8audited financial statements",
        "item8 audited financial statements",
        "item8audited financial statements",
        "item 8: financial statements",
        "item 8:financial statements",
        "item8: financial statements",
        "item8:financial statements",
        "item 8: consolidated financial statements",
        "item 8:consolidated financial statements",
        "item8: consolidated financial statements",
        "item8:consolidated financial statements",
        ]
    """
        Parsing code section
    """

    look={" see ", " refer to ", " included in "," contained in "}

    text1=text.lower()
    text1 = text1[start:]
    a={}

    # Get begin
    for item7 in item7_begins:
        if not item7: 
            print("item7 not found")
            break 
        else: 
             #substr1=text[item7.start()-20:item7.start()]
            #if not any(s in substr1 for s in look):   
                        #print substr1
                #b=text.start()
            begin = text1.find(item7)
                #a.append(b)


        if debug:
            print(item7)
        if begin != -1:
            print(item7)
            break
            
        

    if begin != -1:  # Begin found
        for item7A in item7_ends:
            end = text1.find(item7A, begin + 1)
            if debug:
                print()
            if end != -1:
                break

        if end == -1:  # ITEM 7A does not exist
            for item8 in item8_begins:
                end = text1.find(item8, begin + 1)
                if debug:
                    print(end)
                if end != -1:
                    break

        # Get MDA
        if end > begin:
            #if len[begin:end]>20
            mda = text1[begin:end].strip()
        else:
            end = 0

    return mda, end




file1=[]
for root, dirs, files in os.walk("/Users/lucy/Desktop/allfiles"):
    for file in files:
        if '.txt' in file:
           
            #files.append(os.path.join(root,file))
            with open(os.path.join(root, file), "r") as auto:
                text = auto.read()
                text1=text.lower()
                print(file)
                #print(text1) 
                # test if text.lower() is working 
                

              
      
                # Find MDA section
                mda, end = parse_mda(text1)
                # Parse second time if first parse results in index
                if mda and len(mda.encode('utf-8')) < 1000:
                    mda, _ = parse_mda(text, start=end)
                    #print('error1')
                    #mda_path = os.path.join(mda_dir, file + "mda"+".txt")
                    #print(mda_path+"idiot it doesnt work")
                    #print("writing mda to {}".format(mda_path))
                    #with open(mda_path, 'w') as fout:
                        #fout.write(mda)

                if mda:
                    filename = os.path.basename(os.path.join(root, file))
                    name, ext = os.path.splitext(file)
                    mda_path = os.path.join(mda_dir, name + "mda"+".txt")
                    print("writing mda to {}".format(mda_path))
                    with open(mda_path, 'w') as fout:
                        fout.write(mda)
                else:
                    print("extract mda failed - {}".format(file))
                    with open("/Users/lucy/Desktop/failforall/"+file, "w") as f: 
                        f.write(text1)






