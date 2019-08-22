import re
import sys

recording = False
your_file = "/Users/lucy/Desktop/summer/SummaryDataFile/Aeroquip-Vickers/59198-1999.txt"
start_pattern = "^ITEM 7. MANAGEMENT'S DISCUSSION AND ANALYSIS"
stop_pattern = "^ITEM 8."
output_section = []

for line in open(your_file).readlines():
    if recording is False:
        if re.search(start_pattern, line) is not None:
            recording = True
            output_section.append(line.strip())
    elif recording is True:
        if re.search(stop_pattern, line) is not None:
            recording = False
            sys.exit()
        output_section.append(line.strip())

print(output_section)
