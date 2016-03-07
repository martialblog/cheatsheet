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

    def _getDescriptionWidth(self):
        """
        Returns the width of the longest description in the cheatsheet, so that the output can be dynamic.
        """

        width = 10

        for description in self._configParser['cheats']:
            if len(description) > width:
                width = len(description)

        return width

    def _printInline(self):
        """
        Prints the cheatssheet inline, so that it's grep-able.
        """

        for description in self._configParser['cheats']:
            value = self._configParser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, self._getDescriptionWidth(), value)
            print(output)

    def _printBreakline(self):
        """
        Prints the cheatsheet with newlines
        """

        for description in self._configParser['cheats']:
            value = self._configParser['cheats'][description]
            output = "{0} \n {1}".format(description, value)
            print(output)

    def printCheatSheet(self, breakline):
        """
        Prints the already parsed cheatsheet either inline or with newlines
        """

        if breakline:
            self._printBreakline()
        else:
            self._printInline()

    def indexCheatsheets(self):
        """
        Indexes the available INI files within the config folder
        """

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
            print('Cheatsheet \"'+ requested_cheatsheet +'\" not available')
            exit(1)

def main():
    #Define the command-line arguments... TODO: I gotta clean that up
    argumentParser = argparse.ArgumentParser(description="Command-line cheatsheets")
    argumentParser.add_argument("cheatsheet", help="The cheatsheet you want to see")
    group = argumentParser.add_mutually_exclusive_group()
    group.add_argument("-l", "--inline", action="store_true", help="Output each line, this is default")
    group.add_argument("-b", "--breakline", action="store_true", help="Output break line")
    cmdArguments = argumentParser.parse_args()

    directory = path[0] + "/config/"
    extention = ".ini"

    #Initialize CheatParser
    cp = CheatParser(extention, directory)
    cp.indexCheatsheets()
    cp.parseRequestedCheatSheet(cmdArguments.cheatsheet)
    cp.printCheatSheet(cmdArguments.breakline)

    #Everything is fine and we can exit with 0
    exit(0)

if __name__ == "__main__":
    main()
