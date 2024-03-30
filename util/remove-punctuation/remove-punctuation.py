import os
import csv

def removePunctuation(inputFileName, outputFileName):
    print("Current working directory before")
    print(os.getcwd())
    # os.chdir('../')
    # os.chdir(path)
    # print("Changed dir. \nCurrent working directory after")
    print(os.getcwd())

    with open(inputFileName, 'r') as inputFile:
        outputFile = open(outputFileName, 'r+')
        newLine = []
        for line in inputFile:
            newLine = line.replace('-', ' ').replace(':', ' ').replace('  ', ' ').replace(', ', "\n")
            
    with open(outputFileName, 'r'):
        outputFile2 = open("cap.txt", 'w')
        for line in outputFile:
            newLine = line.title()
            print(newLine)
            outputFile2.writelines(newLine)

if __name__ == "__main__":
    removePunctuation(inputFileName="label-names-to-fix.txt", outputFileName="label-names-fixed.txt")