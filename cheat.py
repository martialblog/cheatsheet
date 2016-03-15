#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

class CheatPrinter:

    def __init__(self, cheatparser):
        self.cheatparser = cheatparser

    def getDescriptionWidth(self):
        """
        Returns the width of the longest description in the cheatsheet, so that the output can be dynamic.
        """

        width = 10

        for description in self.cheatparser['cheats']:
            if len(description) > width:
                width = len(description)

        return width

    def printInline(self):
        """
        Prints the cheatssheet inline, so that it's grep-able.
        """

        width = self.getDescriptionWidth()

        for description in self.cheatparser['cheats']:
            value = self.cheatparser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, width, value)

            print(output)

    def printBreakline(self):
        """
        Prints the cheatsheet with newlines
        """

        for description in self.cheatparser['cheats']:
            value = self.cheatparser['cheats'][description]
            output = "{0} \n {1}".format(description, value)

            print(output)

    def printCheatSheet(self, breakline):
        """
        Prints the already parsed cheatsheet either inline or with newlines
        """

        if breakline:
            self.printBreakline()
        else:
            self.printInline()

class CheatParser:

    def __init__(self, extention, directory):
        self.__available_cheatsheets = {}
        self.__config_directory = directory
        self.__configParser = configparser.ConfigParser()
        self.__file_extension = extention

    def printCheatsheetNotAvailable(self, cheatsheet):
        """
        Print error if cheatsheet isn't there
        """
        print(cheatsheet +' - Cheatsheet not available')

    def indexCheatsheets(self):
        """
        Indexes the available INI files within the config folder
        """

        #TODO: Better way to do this without tempParser?
        tempParser = configparser.ConfigParser()

        for filename in listdir(self.__config_directory):
            try:
                #If the file exsists, put it into the available cheathssheets
                if filename.endswith(self.__file_extension):
                    path_to_file = self.__config_directory + filename
                    tempParser.read(path_to_file)

                    self.__available_cheatsheets[tempParser['main']['name']] = filename

            except configparser.Error as exception:
                print(exception)

    def parseRequestedCheatSheet(self, requested_cheatsheet):
        """
        Parses the requested cheatsheet. If the cheatsheet isn't available the program exits with status 1
        """

        if requested_cheatsheet in self.__available_cheatsheets.keys():
            path_to_file = self.__config_directory + self.__available_cheatsheets[requested_cheatsheet]
            self.__configParser.read(path_to_file)

        else:
            self.printCheatsheetNotAvailable(requested_cheatsheet)
            exit(1)

def main():
    directory = path[0] + "/config/"
    extention = ".ini"
    description = "Cool Command-line Cheatsheets"
    help_general = "The cheatsheet you want to see"
    help_inline = "One cheat per line, this is default"
    help_breakline = "Break lines"

    #Define the command-line arguments.
    argumentParser = argparse.ArgumentParser(description=description)
    argumentParser.add_argument("cheatsheet", help=help_general)
    group = argumentParser.add_mutually_exclusive_group()
    group.add_argument("-l", "--inline", action="store_true", help=help_inline)
    group.add_argument("-b", "--breakline", action="store_true", help=help_breakline)
    cmdArguments = argumentParser.parse_args()

    #Initialize CheatParser
    cparser = CheatParser(extention, directory)
    cparser.indexCheatsheets()
    cparser.parseRequestedCheatSheet(cmdArguments.cheatsheet)

    cprinter = CheatPrinter(cparser)
    cprinter.printCheatSheet(cmdArguments.breakline)

    #Everything is fine and we can exit with 0
    exit(0)

if __name__ == "__main__":
    main()
