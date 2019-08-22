import re
import sys
import os

recording = False
your_file = "sec.txt"
read=[]
for line in open(your_file).readlines(): 
    read.append(line)
    if "ITEM 1A." in read: 
        start_pattern = "ITEM 1."
        stop_pattern = "ITEM 1A."
        output_section = []
        for line in open(your_file).readlines():
            if recording is False:
                if re.search(start_pattern, line) is not None:
                    recording = True
                    output_section.append(line.strip()) # so this code is a loop, we first set recording to true and append line after start-pattern to empty set 
        elif recording is True:
            if re.search(stop_pattern, line) is not None:
                recording = False
                sys.exit()
        output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 
        filename, filetype = os.path.splitext(your_file)
        saveasnew=filename+"int.txt"
        f = open(saveasnew, "w+")
        f.write(text)
        f.close()
        recording = False
        start_pattern = "ITEM 1A."
        stop_pattern = "ITEM 2."
        output_section = []

        for line in open(your_file).readlines():
            if recording is False:
                if re.search(start_pattern, line) is not None:
                    recording = True
                    output_section.append(line.strip()) # so this code is a loop, we first set recording to true and append line after start-pattern to empty set 
            elif recording is True:
                if re.search(stop_pattern, line) is not None:
                    recording = False
                    sys.exit()
            output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 
            saveasnew1=filename+"ext.txt"
            f=open(saveasnew1,"w+")
            f.write(text)
            f

 

 
recording = False
your_file = "sec.txt"
start_pattern = "ITEM 7A"
stop_pattern = "ITEM 8"

for line in open(your_file).readlines():
    if recording is False:
        if re.search(start_pattern, line) is not None:
            recording = True
            output_section.append(line.strip()) # so this code is a loop, we first set recording to true and append line after start-pattern to empty set 
    elif recording is True:
        if re.search(stop_pattern, line) is not None:
            recording = False
            sys.exit()
        output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 

  


filename, filetype = os.path.splitext(your_file)
newfilename=filename+"external.txt"
f = open(newfilename, "w+")
    f.write(text)
    f.close()





#The list of command line arguments passed to a Python script. argv[0] is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
#To loop over the standard input, or the list of files given on the command line, see the fileinput module.

#The following codes is an abbreviated version of the first and execute the function for a second time after the first run 
#import sys
#start_pattern = sys.argv[1]
#stop_pattern = sys.argv[2]
#python name_of_your_script.py "^ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS" "^ITEM 8."


recording = False
your_file = "sec.txt"
start_pattern = "ITEM 7A"
stop_pattern = "ITEM 8"

for line in open(your_file).readlines():
    if recording is False:
        if re.search(start_pattern, line) is not None:
            recording = True
            output_section.append(line.strip()) # so this code is a loop, we first set recording to true and append line after start-pattern to empty set 
    elif recording is True:
        if re.search(stop_pattern, line) is not None:
            recording = False
            sys.exit()
        output_section.append(line.strip()) # then we execute the next step which appends the next line and we set the recording back to false again and iterate through the sample 

  
