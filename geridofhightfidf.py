
import csv


with open ('/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/ngram=13tfidnew.csv', 'w') as outfile:

    with open('/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/ngram=1or2version2.csv', 'r') as csvfile:
        records = csv.reader(csvfile)

        for row in records: 
            if float(row[1])<=8: 
                #print(row[1])
        
                fwriter = csv.writer(outfile)
                fwriter.writerow(row)
            
            
            
    csvfile.close()
    outfile.close()

 