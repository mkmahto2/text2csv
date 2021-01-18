import re
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

with open(inputfile, 'r') as myfile:
     with open(outputfile, 'w') as csv_file:
             for line in myfile:
                     fileContent = re.sub("\t", ",", line)
                     csv_file.write(fileContent)
