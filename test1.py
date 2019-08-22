

import re
import sys
import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

recording = False

f = open("/Users/lucy/Desktop/summer/SummaryDataFile/Aeroquip-Vickers/59198-1999.txt", "r")
start_pattern = "^ITEM 7."                  
stop_pattern = "^ITEM 7A."
output_section=[]
    
for line in f: 
    if recording is False:
        if re.search(start_pattern, line) is not None:
            recording = True
            output_section.append(line.strip()) # so this code is a loop, we first set recording to true and append line after start-pattern to empty set 
                        #lowercase : boolean (default=True)
                        #' '.join([word for word in line.lower().split()])
                        #stopwords = [word.decode('utf-8') for word not in stopwords.words('english')]
    elif recording is True:
        if re.search(stop_pattern, line) is not None:
            recording = False
            sys.exit()
            output_section.append(line.strip())

print(output_section)
