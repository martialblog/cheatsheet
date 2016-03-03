#!/usr/bin/python3
import sys
import argparse
import os
import io
import configparser

desc = "Cool Command-Line Cheatsheets"
extension = ".ini"
cheatsheets = {}
configDir = sys.path[0] + "/config/"
cfgParser = configparser.ConfigParser()
argParser = argparse.ArgumentParser(description=desc)

#Command Line Arguments
group = argParser.add_mutually_exclusive_group()
group.add_argument("-l", "--inline", action="store_true", help="Output each line, this is default")
group.add_argument("-b", "--breakline", action="store_true", help="Output break line")
argParser.add_argument("cheatsheet", help="The cheatsheet you want to see")

def printInline():

    width = 10

    for key in cfgParser['cheats']:
        if len(key) > width:
            width = len(key)

    for key in cfgParser['cheats']:
        output = "{0:<{1}} {2}".format(key, width, cfgParser['cheats'][key])
        print(output)

def printBreakline():

    for key in cfgParser['cheats']:
        output = "{0} \n {1}".format(key, cfgParser['cheats'][key])
        print(output)

def indexCheatsheets():

    tmpParser = configparser.ConfigParser()

    for filename in os.listdir(configDir):
        try:
            if filename.endswith(extension):
                tmpParser.read(configDir + filename)
                cheatsheets[tmpParser['main']['name']] = filename
        except configparser.MissingSectionHeaderError as exception:
            print(exception)

def main():

    args = argParser.parse_args()

    indexCheatsheets()

    if args.cheatsheet in cheatsheets.keys():
        cfgParser.read(configDir + cheatsheets[args.cheatsheet])

        if args.breakline:
            printBreakline()
        else:
            printInline()

        exit(0)

    else:
        print('Cheatsheet \"'+ args.cheatsheet +'\" not available')
        exit(1)

if __name__ == "__main__":
    main()
