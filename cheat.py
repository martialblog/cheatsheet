#!/usr/bin/python3
import sys
import argparse
import os
import io
import configparser

# TODO
# Check if INI syntax is OK
# Colored or formated output... better readable anyways

desc = "Cool Command-Line Cheatsheets"
extension = ".ini"
cheatsheets = []
configDir = "."
cfgParser = configparser.ConfigParser()
argParser = argparse.ArgumentParser(description=desc)

#Command Line Arguments
group = argParser.add_mutually_exclusive_group()
group.add_argument("-l", "--inline", action="store_true", help="Output each line, this is default")
group.add_argument("-b", "--breakline", action="store_true", help="Output break line")
argParser.add_argument("cheatsheet", help="The cheatsheet you want to see")

def printInline():
    #print inline
    for key in cfgParser['cheats']:
        print(key +": "+ cfgParser['cheats'][key])

def printBreakLine():
    #print breakline
    for key in cfgParser['cheats']:
        print("\n"+ key +":\n"+ cfgParser['cheats'][key])

def createFileList(extension):
    for file in os.listdir(configDir):
        if file.endswith(extension):
            cheatsheets.append(file)

def main():
    args = argParser.parse_args()
    filename = args.cheatsheet + extension
    createFileList(extension)

    if not os.path.exists(filename):
        print("No such file:", filename)
        exit(1)
    else:
        cfgParser.read(filename)

    if args.inline:
        printInline()
    elif args.breakline:
        printBreakLine()
    else:
        printInline()

if __name__ == "__main__":
    main()
