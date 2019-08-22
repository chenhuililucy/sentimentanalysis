
import re
import sys
import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer


import io

output_section=[]

#corpus=nltk.corpus.reader.PlaintextCorpusReader("/Users/lucy/Desktop/summer/SummaryDataFile",r'.*', encoding='latin-1'):
for root, dirs, files in os.walk("/Users/lucy/Desktop/summer/SummaryDataFile"):
    for file in files:
        with open(os.path.join(root, file), "r") as auto:
            for line in auto: 
                if "ITEM 7A." in file:
                    recording = False
                    start_pattern = "ITEM 7."
                    stop_pattern = "ITEM 7A."
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
                            output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 
                        #lowercase : boolean (default=True)
                        #' '.join([word for word in line.lower().split()])
                        #stopwords = [word.decode('utf-8') for word not in stopwords.words('english')]
                elif "Item 7A" in file:
                    recording = False
                    start_pattern = "Item 7"
                    stop_pattern = "Item 7A"
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
                            output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 
                        #lowercase : boolean (default=True)
                        #' '.join([word for word in line.lower().split()])
                        #stopwords = [word.decode('utf-8') for word not in stopwords.words('english')]
                elif "ITEM 8" in file:
                    recording = False
                    start_pattern = "ITEM 7"
                    stop_pattern = "ITEM 8"
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
                            output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 
                        #lowercase : boolean (default=True)
                        #' '.join([word for word in line.lower().split()])
                        #stopwords = [word.decode('utf-8') for word not in stopwords.words('english')]


output = ''.join(output_section)
f = open("dictionaryraw.txt", "w+")
f.write(output)
f.close()


#vectorizer = TfidfVectorizer()
#X = vectorizer.fit_transform(output.split('\n')
#file1 = open("dictionary", "w+", encoding='latin-1')
#file1.write(vectorizer.get_feature_names())
#file1.close()




# lowercase : boolean (default=True)
#SyntaxError: unexpected EOF while parsing