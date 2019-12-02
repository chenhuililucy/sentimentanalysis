
import csv
with open('h.csv', 'r',encoding='utf-8', errors='ignore') as citation:
    reader = csv.reader(citation)
    for row in reader: 
        print(row[0]+".,("+row[1]+")."+row[2]+".") 

