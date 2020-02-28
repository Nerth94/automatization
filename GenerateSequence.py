# Prepared by PLE
# Script version: 1.0.0
# Origin date: 28-02-2020


import os
from tkinter import filedialog

errorCounter = 0
tcCounter = 0
sequenceFile = open("PS31TM_AUTOMATIC_SEQUENCE.sq", "w+")

folderPath = filedialog.askdirectory()

chosenFilesInDirectory = []
for root, dir, chosenTestCases in os.walk(folderPath):
    for singleTestCase in chosenTestCases:
        if '.tc' in singleTestCase and '.tcl' not in singleTestCase:
            chosenFilesInDirectory.append(os.path.join(root, singleTestCase))

for singleFile in chosenFilesInDirectory:
    with open(singleFile, 'r+') as openTestCase:
        row = openTestCase.readlines()
        for line in row:
            if line.startswith('#@TYPE'):
                tag, automationType = line.split()
                if automationType == 'AUTO':
                    print(singleFile)
                    #print(singleTestCase)
                    tcCounter += 1

# for singleFile in chosenFilesInDirectory:
# print(singleFile)
# tcCounter += 1

print(f'Number of included automatic test cases: {tcCounter}')
# print(f'Number of errors: {errorCounter}')
input("Press any key to continue...")
