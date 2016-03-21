#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

class Printer():

    def __init__(self, configparser):
        self._configparser = configparser
        self._width = 10
        self.calculateDescriptionWidth()

    def getWidth():
        return self._width

    def calculateDescriptionWidth(self):
        """
        Returns the width of the longest description in the cheatsheet, so that the output can be dynamic.
        """

        for description in self._configparser['cheats']:
            if len(description) > self._width:
                self._width = len(description)

class InlinePrinter(Printer):

    def printCheatSheet(self):
        """
        Prints the cheatssheet inline, so that it's grep-able.
        """

        for description in self._configparser['cheats']:
            value = self._configparser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, self.getWidth(), value)

            print(output)

class BreaklinePrinter(Printer)

    def printCheatSheet(self):
        """
        Prints the cheatsheet with newlines
        """

        for description in self._configparser['cheats']:
            value = self._configparser['cheats'][description]
            output = "{0} \n {1}".format(description, value)

            print(output)

class CheatHandler:

    def __init__(self, extention, directory):

        self.__configParser = configparser.ConfigParser()
        self.__available_cheatsheets = {}
        self.__config_directory = directory
        self.__file_extension = extention

    def getConfigParser(self):

        return self.__configParser

    def printCheatsheetNotAvailable(self, cheatsheet):

        print(cheatsheet +' - Cheatsheet not available')

    def indexCheatsheets(self):
        """
        Indexes the available INI files within the config folder
        """

        tempParser = configparser.ConfigParser()

        for filename in listdir(self.__config_directory):
            try:
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
    group.add_argument("-l", "--inline", action="store_const", help=help_inline)
    group.add_argument("-b", "--breakline", action="store_const", help=help_breakline)
    cmdArguments = argumentParser.parse_args()

    #Initialize CheatHanlder
    chandler = CheatHandler(extention, directory)
    chandler.indexCheatsheets()
    chandler.parseRequestedCheatSheet(cmdArguments.cheatsheet)

    #printer = either Break or Inline printer
    #printer.printCheatSheet()

    #Everything is fine and we can exit with 0
    exit(0)

if __name__ == "__main__":
    main()
