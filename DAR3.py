import csv
import requests
import re
from bs4 import BeautifulSoup 
# DAR Debug
# Extract based on https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python/8201491
import os
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files)) # End DAR Debug

with open('out50-90.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        fn1 = line[0]
        fn2 = re.sub(r'[/\\]', '', line[1])
        fn3 = re.sub(r'[/\\]', '', line[2])
        date = line[3]
        print(date)
        twodigityear=date[-2:]
        print(twodigityear)
        twodigityear=int(twodigityear)
        if twodigityear<50:
            year = 2000 + twodigityear 
        else: 
            year= 1900 +twodigityear 
        print(year)
        year=str(year)
        saveas = '-'.join([fn1, fn4])
        saveasnew = saveas.replace("/", "~") + ".txt"
        # Reorganize to rename the output filename.
        url =  line[4].strip()
        #DAR Debug
        print(line[0])
        print(line[1])
        print(line[2])
        print(line[3])
        print(line[4])
        print(url) # End DAR Debug

        bodytext=requests.get(url).text 
        parsedContent=BeautifulSoup(bodytext, 'html.parser')
        for script in parsedContent(["script", "style"]): 
            script.extract()
        text = parsedContent.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk) 
        #with open(saveasnew, 'ab') as f: # DAR Changed from saveas to saveasnew to remove '/' from filename
            #f.write(requests.get('%s' % text).content)
            #f.print(file, 'downloaded and wrote to text file')
            #f.close()

        # File output code from https://www.guru99.com/reading-and-writing-files-in-python.html
        f = open(saveasnew, "w+")
        f.write(text)
        f.close()
