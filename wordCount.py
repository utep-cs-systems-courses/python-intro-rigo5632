# Libraries
import sys
import re
import os

# Checks for 3 correct arguments
if len(sys.argv) != 3:
    print('Error')
    exit()

inputFile  = sys.argv[1]
outputFile = sys.argv[2]

# Checks if input file exists
if not os.path.exists(inputFile):
    print(inputFile, 'file does not exists')
    exit()

#Dictionary
wordCount = {}

# reads input file and adds new words to dictionary
with open(inputFile, 'r') as textFile:
    words = re.split('\W', textFile.read())

    for word in words:
        key = word.lower()

        if key != '':
            if wordCount.get(key) == None:
                wordCount[key] = 1
            else:
                wordCount[key] += 1
    textFile.close()
    newFile = open(outputFile, 'w')

# writes data from dictionary into outputfile
for key in sorted(wordCount):
    newFile.write('%s %d\n' %(key, wordCount[key]))
newFile.close()


