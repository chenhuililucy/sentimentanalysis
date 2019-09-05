

import os 
import shutil

orgdir="/Users/lucy/Desktop/dictionary"
newdir="/Users/lucy/Desktop/newdic"

for f in os.listdir('/Users/lucy/Desktop/dictionary'): 
    with open f as read: 
        if len(read)>100:
        shutil.move(f,newdir)


        