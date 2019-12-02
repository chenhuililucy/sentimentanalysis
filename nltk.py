 

 			   How to install NLTK through Pip    

 

 

Downloading and installing Pip: 

 https://www.youtube.com/watch?v=yBdZZGPpYxg (mac)  

            https://www.youtube.com/watch?v=zPMr0lEMqpo (windows) 

 

Downloading NLTK through Pip:  

https://www.nltk.org/install.html 

 

 

Mac version of installing NLTK through Pip: 

 

Codes: (terminal)  

pip install --user -U nltk 

python  

>>> import nltk 

>>> nltk.download() 

 

 

import numpy as np 

import matplotlib.pyplot as plt 

import pandas as pd 

 

If your pandas is not installed on your computer, see installation instructions at:  

 

https://github.com/pandas-dev/pandas/issues/11604 

 

----------------------------------------------------------------------------------- 

 

 

   Web scraping from Edgar  

 

It is possible to export from edgar using the following codes after installing edgar in terminal and importing it into python 

 

import edgarcompany = edgar.Company("Oracle Corp", "0001341439") 

tree = company.getAllFilings(filingType = "10-K") 

docs = edgar.getDocuments(tree, noOfDocuments=5) 



 

 

Please see this instruction document for more description: 

https://pypi.org/project/edgar/ 

 

Other documents with similar instructions include:  

https://pypi.org/project/python-edgar/ (I cannot execute the download directory instruction on this document) 

 

https://www.youtube.com/watch?v=gfpmKkxhb9M (this seems to be very useful but I have not had a detailed look at it yet)  

 

This video suggests alternatives to the SEC EDGAR database  

https://www.youtube.com/watch?v=IKznctrWlrM 

 

 

 

 

 

If you want to download EDGAR reports programmatically, then determining the URL is just the first step. You'll need to perform at least four steps: 

Send a request to the URL and receive an HTML response. 

Parse the HTML to find the URL(s) of the report(s) of interest. 

For each report of interest, send a request to the report's URL. 

Parse the response to download the desired report. 



------------------------------------------------------------------------------ 

 

Importing directly from URL 

 

 

import urllib2  # the lib that handles the url stuff 

data = urllib2.urlopen(target_url) # it's a file like object and works just like a file 

for line in data: # files are iterable    print line 

 

 

https://www.sec.gov/Archives/edgar/data/1045810/000104581019000023/nvda-2019x10k.htm 

 

from urllib.request import urlopen 

link = "insert link here" 

f = urlopen(link) 

myfile = f.read() 

print(myfile) 

 

----------------------------------------------------------------------------------- 

   

 

    Bayes data training  

 

Data training with classifier  

  

 

https://pythonprogramming.net/naive-bayes-classifier-nltk-tutorial/ 

 

------------------------------------------------------------------------------------ 

 

 

 Finding word stem 

 

Source: https://pythonprogramming.net/stemming-nltk-tutorial/ 

 

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
ps = PorterStemmer() 

example_words = ["python","pythoner","pythoning","pythoned","pythonly"] 

 
for w in example_words:    
    print(ps.stem(w)) 


def stem(word):  
    for suffix in [‘ing’, ‘ly’, ‘ed’, ‘ious’, ‘ies’, ‘ive’, ‘es’, ‘s’,’ment’]:  
        if word. endwith(suffix)   
        words = word_tokenize(new_text) for w in words:
        print(ps.stem(w)) 

 

 

#Import data from computer  

#shows reading from a text file  

print("Opening and closing the file.") 

text_file = open("text file name","r") 

text_file.close() 

 

f = open ('text file name') 

>>> raw = f.read() 

>>> print (f.read) 

 

 

>>> f= open("textfilename","w+") 

>>> for i in range(10): 

     f.write("This is line %d\r\n" % (i+1) 

>>> f.close() 

 

 

------------------------------------------------------------------------------------------------------------- 

 

 Sentiment analysis systems  

 

https://www.pingshiuanchua.com/blog/post/simple-sentiment-analysis-python?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com 

 

Method 1: Importing from Google Cloud 

Link: https://www.youtube.com/watch?v=ji1DWCTI05A 

 

from google.cloud import language 

 
 

def language analysis(text): 

    client =language,Client() 

    document =client.document_from_text(text) 

    sent_analysis = document.analyze_sentiment() 

    print(dir(sent_analysis)) 

    sentiment = sent_analysis.sentiment 

    ent_analysis = document.analyze_entities() 

    entities = ent_analysis.entities 

    return sentiment,entities 

 
 

example_text= 'insert example text here' 

 
 

sentiment,entities = language_analysis(example_text)  

print (sentiment.score, sentiment.magnitude) 

 
 

for e in entities  

        print(e.name, e.entity_type, e.metadata, e.salience) 

 

https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis 

 

Method 3:  Vader  

 

https://pythonprogramming.net/sentiment-analysis-python-textblob-vader/ 

 

 

Stop words and accuracy checkers: 

 

https://towardsdatascience.com/sentiment-analysis-with-python-part-2-4f71e7bde59a 

 

https://www.youtube.com/watch?v=ji1DWCTI05A 

------------------------ 

 

 

 

 

 

 

     Notes from NLTK Reference book  

 

https://www.nltk.org/book/ch01.html 

 

 

NTLK notes from book: commands  

(replace green) 

 

General NTLK commands  

 

text name. concordance (“search phrase”)  

shows every occurrence of a given word in imported text  

text name. similar (“search phrase”)  

shows words with similar meanings in context   

lexical dispersion plot: determines the location of a word in a plot  

Command: text name. dispersion_plot ([“search phrase list, separated by commas”])  

(needs to have installed matplotlib)  

len (text name)  

counts length of a text  

sorted(set(text name)) 

tokenizing and collapsing words in text  

len(set(text name))/len(text name)  

calculating lexical richness  

 

Indexing lists  

      text name[no of word] 

      Picks out the “...”th word in the text  

      text name.index(‘word’) 

      Performs function in reverse  

      text name[no of word: no of word] 

      Performs ‘slicing’ , display all the words selected from beginning number of words to last number of words  

 

 

General python commands  

Defines function with a new name 

def command name (text): 

                  return function  

 

Lists  

Define list command: List name = [‘search phrase list’] 

Adding two lists: eg. list 1 +list 2  

 

 

Strings  

name = ‘word’ 

 First define a string  

Then you can use python to recall the “nth” word in the string 

 

Eg .  

name[0]  

 Shows first letter of string 

name[:4] 

Shows first 4 letters of string  

 

 

Statistics 

 

Frequency distribution 

 

fdist1 = FreqDist (text name)  

print (fdist 1) 

 

Find distribution of the most common 50 phrases  

>>> fdist1.most_common(50) 

 

>>> fdist1['whale'] 

 
 

 

 

Selection of words 

 

V = set(text1)  

long_words= [w for w in V if len(w) > 15] 

sorted(long_words) 

 

Search for words of a certain length, or longer than a certain length in text  

 

Example 

Description 

fdist = FreqDist(samples) 

create a frequency distribution containing the given samples 

fdist[sample] += 1 

increment the count for this sample 

fdist['monstrous'] 

count of the number of times a given sample occurred 

fdist.freq('monstrous') 

frequency of a given sample 

fdist.N() 

total number of samples 

fdist.most_common(n) 

the n most common samples and their frequencies 

for sample in fdist: 

iterate over the samples 

fdist.max() 

sample with the greatest count 

fdist.tabulate() 

tabulate the frequency distribution 

fdist.plot() 

graphical plot of the frequency distribution 

fdist.plot(cumulative=True) 

cumulative plot of the frequency distribution 

fdist1 |= fdist2 

update fdist1 with counts from fdist2 

fdist1 < fdist2 

test if samples in fdist1 occur less frequently than in fdist2 

 

 

Function 

Meaning 

s.startswith(t) 

test if s starts with t 

s.endswith(t) 

test if s ends with t 

t in s 

test if t is a substring of s 

s.islower() 

test if s contains cased characters and all are lowercase 

s.isupper() 

test if s contains cased characters and all are uppercase 

s.isalpha() 

test if s is non-empty and all characters in s are alphabetic 

s.isalnum() 

test if s is non-empty and all characters in s are alphanumeric 

s.isdigit() 

test if s is non-empty and all characters in s are digits 

s.istitle() 

test if s contains cased characters and is titlecased (i.e. all words in s have initial capitals) 

 

Method 

Functionality 

s.find(t) 

index of first instance of string t inside s (-1 if not found) 

s.rfind(t) 

index of last instance of string t inside s (-1 if not found) 

s.index(t) 

like s.find(t) except it raises ValueError if not found 

s.rindex(t) 

like s.rfind(t) except it raises ValueError if not found 

s.join(text) 

combine the words of the text into a string using s as the glue 

s.split(t) 

split s into a list wherever a t is found (whitespace by default) 

s.splitlines() 

split s into a list of strings, one per line 

s.lower() 

a lowercased version of the string s 

s.upper() 

an uppercased version of the string s 

s.title() 

a titlecased version of the string s 

s.strip() 

a copy of s without leading or trailing whitespace 

s.replace(t, u) 

replace instances of t with u inside s 

 

 

 

 

 

len(text1) # The length of text1 

text2 = text1.split(' ') #same as the function of word.tockenize() 

# Return a list of the words in text2, separating by ' '. 

 len(text2) 

Len(set(text4)) #gives you all the words, removes repetitions 

Len (w.lower.() for w in text 4)  

s. startswith (t)  

s. endswith(t)  

t in s 

s. isupper() ; s.istitle() 

s.strip() # takes all whitespace from front of string 

 

 

 

 

 

Keyboard Short cut 

Control n  

      to Open new file  

 

File Menu 

New window : Create a new editing window. Shortcut key : Ctrl+N 

Open : Open an existing file. Shortcut key : Ctrl+O 

Open module : Open an existing module. Shortcut key : Alt+M 

Class browser : Show classes and methods in current file. shortcut key : Alt+C 

Save : Save current window to the associated file. Shortcut key : Ctrl+S 

Save As : Save current window to new file, which becomes the associated file. Shortcut key : Ctrl+shift+S 

Save Copy As : Save current window to different file without changing the associated file. Shortcut key : Alt+shift+S 

Print window. Shortcut key : Ctrl+P 

Close : Close current window (asks to save if unsaved). Shortcut key : Alt+F4 

Exit : Close all windows and quit IDLE (asks to save if unsaved). Shortcut key : Ctrl+Q 

 

Others  

 

Executing Python commands from a shell script  

https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script 