						Contributions: 

•	Attribution theory dictionary and reading engine, similar to LM, but with more complex semantic structures that can be reapplied to any research relating to internal, external or performance based 10-K vocabulary, or any financial use to extract components of 10-Ks that contain the aforementioned language
•	Test the correlation between performance and internal and external sentiments 
•	Goodness of fit R value => when the year goes bad the correlation weakens
•	Gets literature review condensed 



				Online code database which does the following: 

•	Formalize heuristics for regex extraction of a specific part of 10-K eg. MD&A  
•	In depth discussion of web scrapping efficiency 
•	Discussion of optimal method to optimize text extraction, parsing of large quantity of text data speed (writing to list, numpy arrays, using itertools) 
•	Data structure to maximize storage of text data 
•	Systematic way to select testing set (cik)  


					 10-K filing complete extraction

					      Extract raw files: 

extracthtml.py
convertcsv.py
DAR0.py

Missing: parsing heuristics but introduced in LM’s codes

						Using LM database:

renamefiles.py
movenewdirs.py
movefiles.py


  					       MD&A extraction

Original testing concepts/trials: 
For loop + Boolean trails: tfidftrial1.py, test 2.py, extractsections.py

Extract MD&A sample codes: 
onlinecodes.py / MDA.py
edgar1.py

Finalized:
newMDA.py, wordcount<100.py

					   Item 13 extraction: 
convertcsv1.py
Item13.py
sortfailv4.py
extractpreequitysection.py


					      Vocabulary 

tfidfvectorizer.py
getridofhightfidf.py


					  Building dictionary

senttockenized.py
regexmatchwords.py
dicpart1.py
dicpart3v2.pu
dicpart2.py

Reference LM’s code: Generic_Parser.py
Others: LM stopwords.py






