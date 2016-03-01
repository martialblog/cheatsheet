#/bin/python3
import sys
import getopt
import os
import io
import configparser

# TODO
# Parse command line options and shit
 # -l lines
 # Add file to staging ares: git add filename
 # -b break
 # Add file to stating area:
 # git add filename

extension = ".ini"
cheatsheets = []
configDir = "."
cfg = configparser.ConfigParser()

def printInline():
    #print inline
    for key in cfg['cheats']:
        print(key +": "+ cfg['cheats'][key])

def printBreakLine():
    #print breakline
    for key in cfg['cheats']:
        print("\n"+ key +":\n"+ cfg['cheats'][key])

def createFileList(extension):
    for file in os.listdir(configDir):
        if file.endswith(extension):
            cheatsheets.append(file)

def checkAvailableCheatSheets(name):
    isAvailable = False
    #make list of available .cs
    #check if name exists
    return isAvailable

def main():
    #ParseCommandLineParameter
    #MakeFileList
    #Parse shit
    #Is argv1 available
    #print shit
    createFileList(extension)

    cfg.read('git.ini')
    printInline()
    printBreakLine()

if __name__ == "__main__":
    main()
