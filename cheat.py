#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

class CheatParser:

    def __init__(self, extention, directory):
        self._available_cheatsheets = {}
        self._config_directory = directory
        self._configParser = configparser.ConfigParser()
        self._file_extension = extention

    def getDescriptionWidth(self):
        """
        Returns the width of the longest description in the cheatsheet, so that the output can be dynamic.
        """

        width = 10

        for description in self._configParser['cheats']:
            if len(description) > width:
                width = len(description)

        return width

    def printInline(self):
        """
        Prints the cheatssheet inline, so that it's grep-able.
        """

        for description in self._configParser['cheats']:
            value = self._configParser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, self.getDescriptionWidth(), value)

            print(output)

    def printBreakline(self):
        """
        Prints the cheatsheet with newlines
        """

        for description in self._configParser['cheats']:
            value = self._configParser['cheats'][description]
            output = "{0} \n {1}".format(description, value)

            print(output)

    def printCheatsheetNotAvailable(self, cheatsheet):
        """
        Print error if cheatsheet isn't there
        """
        print(cheatsheet +' - Cheatsheet not available')

    def printCheatSheet(self, breakline):
        """
        Prints the already parsed cheatsheet either inline or with newlines
        """

        if breakline:
            self.printBreakline()
        else:
            self.printInline()

    def indexCheatsheets(self):
        """
        Indexes the available INI files within the config folder
        """

        #TODO: Better way to do this without tempParser?
        tempParser = configparser.ConfigParser()

        for filename in listdir(self._config_directory):
            try:
                #If the file exsists, put it into the available cheathssheets
                if filename.endswith(self._file_extension):
                    path_to_file = self._config_directory + filename
                    tempParser.read(path_to_file)

                    self._available_cheatsheets[tempParser['main']['name']] = filename

            except configparser.Error as exception:
                print(exception)

    def parseRequestedCheatSheet(self, requested_cheatsheet):
        """
        Parses the requested cheatsheet. If the cheatsheet isn't available the program exits with status 1
        """

        if requested_cheatsheet in self._available_cheatsheets.keys():
            path_to_file = self._config_directory + self._available_cheatsheets[requested_cheatsheet]
            self._configParser.read(path_to_file)

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
    cp = CheatParser(extention, directory)
    cp.indexCheatsheets()
    cp.parseRequestedCheatSheet(cmdArguments.cheatsheet)
    cp.printCheatSheet(cmdArguments.breakline)

    #Everything is fine and we can exit with 0
    exit(0)

if __name__ == "__main__":
    main()
