import matplotlib.pyplot as plt
from scipy.stats import zipf

lst=[]

with open('/Users/lilucy/Desktop/zipfdata.csv','w') as csvfile:
    fieldnames=['word','count']
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    for row in records:
        wordtokens=row[0].lower()
        count=row[1].lower()
        lst.append((count,wordtokens))


plt.bar([key for val, key in lst], [val for val, key in lst], color='limegreen')
alpha = 1.37065874
total = sum([p for p, c in lst])
plt.plot(range(len(lst)), [zipf.pmf(p, alpha) * total for p in range(1, len(lst) + 1)], color='crimson', lw=3)
plt.ylabel("Frequency")
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()

