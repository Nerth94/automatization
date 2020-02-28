# Prepared by PLE
# Script version: 1.0.2
# Origin date: 6-08-2019
# Last change date: 21-02-2020
# Last changes made: edited order of inserting variants to the test case. Refactored variables' and functions' names.
# How to use: run the script and choose folder in which test cases shall be updated. Script recognizes variant by prefix in the test case name (now implemented: PS31TM_ALL_*, PS31TM_TIM_ALL_*, PS31TM_HS_*, PS31TM_LS_*, PS31TM_COM_*, PS31TM_EU_*, PS31TM_US_*, P22_*).

import os
from tkinter import filedialog


def InsertTagAll():
    for eachVariant in chosenVariant:
        wholesingleFile = open(singleFile).read().replace(f'{lineWithBTL}', f'{lineWithBTL}\n{lineWithVariant}{eachVariant}')
        output = open(singleFile, 'w')
        output.write(wholesingleFile)
        output.close()


def InsertTag():
    wholesingleFile = open(singleFile).read().replace(f'{lineWithBTL}', f'{lineWithBTL}\n{lineWithVariant}{chosenVariant}')
    output = open(singleFile, 'w')
    output.write(wholesingleFile)
    output.close()


errorCounter = 0
tcCounter = 0
lineWithBTL = '#@BTL       2.2'
lineWithVariant = '#@VARIANT   '

HS_line = 'HS'
HS_phase = 'TIM_HS'
LS_line = 'LS'
LS_phase = 'TIM_LS'
COM_line = 'COM'
COM_phase = 'TIM_COM'
EU_line = 'EU'
EU_phase = 'TIM_EU'
US_line = 'US'
US_phase = 'TIM_US'
BSG_line = 'P22'
BSG_phase = 'P22_BSG_RQ'
TIM_ALL_phase = 'TIM_ALL'
ALL_phase = 'ALL'

folderPath = filedialog.askdirectory()

chosenFilesInDirectory = []
for root, dir, chosenTestCases in os.walk(folderPath):
    for singleTestCase in chosenTestCases:
        if '.tc' in singleTestCase and '.tcl' not in singleTestCase:
            chosenFilesInDirectory.append(os.path.join(root, singleTestCase))

for singleFile in chosenFilesInDirectory:
    print(singleFile)
    tcCounter += 1
    with open(singleFile, 'r+') as openTestCase:
        row = openTestCase.readlines()
        for line in row:
            if line.startswith('#@NAME'):
                tag, name = line.split()
                project, chosenVariant, *_ = name.split('_')
            if line.startswith('#@VARIANT'):
                clear_variant = open(singleFile).read().replace(f'{line}', '')
                output2 = open(singleFile, 'w')
                output2.write(clear_variant)
                output2.close()
            if line.startswith('#@BTL'):
                clear_btl = open(singleFile).read().replace(f'{line}', f'{lineWithBTL}\n')
                output3 = open(singleFile, 'w')
                output3.write(clear_btl)
                output3.close()
        openTestCase.close()

    if chosenVariant == HS_line:
        chosenVariant = [US_phase, EU_phase, COM_phase, HS_phase]
        InsertTagAll()
    elif chosenVariant == LS_line:
        chosenVariant = [LS_phase, BSG_phase]
        InsertTagAll()
    elif chosenVariant == COM_line:
        chosenVariant = COM_phase
        InsertTag()
    elif chosenVariant == EU_line:
        chosenVariant = EU_phase
        InsertTag()
    elif chosenVariant == US_line:
        chosenVariant = US_phase
        InsertTag()
    elif project == BSG_line:
        chosenVariant = BSG_phase
        InsertTag()
    elif chosenVariant == 'TIM':
        chosenVariant = [US_phase, EU_phase, COM_phase, LS_phase, HS_phase, TIM_ALL_phase]
        InsertTagAll()
    elif chosenVariant == ALL_phase:
        chosenVariant = [US_phase, EU_phase, COM_phase, LS_phase, HS_phase, TIM_ALL_phase, BSG_phase, ALL_phase]
        InsertTagAll()
    else:
        print('Error - unknown variant!')
        errorCounter += 1

print(f'Number of updated test cases: {tcCounter}')
print(f'Number of errors: {errorCounter}')
input("Press any key to continue...")