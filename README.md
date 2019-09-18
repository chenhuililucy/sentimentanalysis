# sentimentanalysis
experimental codes for a summer research project 

This is just to clarify that not all of the codes here are 100% my own. Some of them are codes I've modified based on online codes. 
				
	
			----------------------------------


Sorry about uploading so many python files with confusing names! I will talk about what they are each about here: 


In terms of data extraction, there are two ways: 


Method1: 

First you need to understand the formats of Edgar datafile, unfortunately they cannot be crawled in raw text form. They are stored in .txt form, .html form, java and xml form. I first tried to use codes provided by Kai Chen here http://kaichen.work/?p=681 t
To crawl data in the form of .txt: I used two pieces of codes: 1. Find paths to raw text filing 2. Bulk download Edgar files using paths 3. Parse these datafiles with beautiful soup. However, I realized that the datafiles in txt forms are like 1000 pages long and it’s really slow: so I switched to downloading these files in html form. 

1. Use master index csv I requested from Kaichen here: http://kaichen.work/?p=946,

2. According to the name of the company given on the Forbes website, search for each of their CIK (a company might have several CIKS 

3. Drop all columns that do not contain the ciks of interest, drop all columns that do not contain string ’10-K’ . You can do this in SQLite or STATA (Note here that there are different types of ’10-K’ documents : 10-K-A is amended filings associated with restatements of financials, incorporates Part III/ Proxy information (this document is basically useless if it doesn’t contain the MD&A section); 10-K405: used to indicate that an officer or director of a company failed to file a Form 4 on time, Form 4 is used to disclose insider trade information; 10-KSB is an optional form for annual and transition reports of small business issuers) 

4. Use the convertcsv.py file to convert your csv file to obtain an output file with a directory a page on Edgar with link to 10-K filing. Store this as your first output file. 

5. Use the extracthtml.py file to convert your first output file to a second csv output file with exact locations to the 10-K filings.

6. Use DAR3.py and input your second csv output file to output parsed 10-K filings into a folder. 

Method 2: (I AM USING THIS METHOD NOW) 

I thought method 1 was really slow, and I stumbled upon a google drive with all the data files and store it on my harddisc (this takes up 10GB storage space so you need to be prepared as it might ruin your computer). https://drive.google.com/drive/folders/1tZP9A0hrAj8ptNP3VE9weYZ3WDn9jHic

I wrote two pieces of codes, renamefiles.py rename these files to cik-year form and movenewdir.py moves the files in cik year to folders with their specific company names in your csv file (the file with your selected company names and their matching ciks) 

								————————————————

Extracting MD&A section

I have tried to write my own codes and modify online codes for this. But this has not been very successful.
First method I tried was using for loops: in extractsections.py. However, for some reason my codes failed to work. 
I then found 2 people’s Githubs that have relevant codes. I tried to modify their codes ins ways that suit what we are doing. They are labeled as onlinecodes and MD&A respectively. 
I finally found a way to output some info but still could not match all the MD&A sections due to formatting inconsistencies. My codes newMDA.py outputs about 50% of all MD&A sections. 

Update 3rd September 
I figured out an iterative error in my codes which improved my accuracy to up to find 75% of all MDA sections. However, the problem now is that some firms do not state "item 7" explicitly as they are already included in their letter to shareholders. I have found that letter to shareholders is usually labeled as item EX-13 and I am doing some troubleshooting.  

							



