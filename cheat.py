#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

class Printer:

    def __init__(self, configparser):
        self._configparser = configparser

    def printCheatSheet(self):
        raise NotImplementedError

class InlinePrinter(Printer):
    """
    Prints the cheatssheet inline, so that it's grep-able.
    """

    def __init__(self, configparser):
        super().__init__(configparser)
        self._width = self.calculateDescriptionWidth()

    def calculateDescriptionWidth(self):
        width = 10

        for description in self._configparser['cheats']:
            if len(description) > width:
                width = len(description)

        return width

    def printCheatSheet(self):
        for description in self._configparser['cheats']:
            value = self._configparser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, self._width, value)

            print(output)

class BreaklinePrinter(Printer):
    """
    Prints the cheatsheet with newlines
    """

    def __init__(self, configparser):
        super().__init__(configparser)

    def printCheatSheet(self):
        for description in self._configparser['cheats']:
            value = self._configparser['cheats'][description]
            output = "{0} \n {1}".format(description, value)

            print(output)

class CheatHandler:
    """
    Indexes the available INI files within the config folder and parses the requested file
    """

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
    group.add_argument('-l', help=help_inline, action='store_const', dest='printer', const='InlinePrinter')
    group.add_argument('-b', help=help_breakline, action='store_const', dest='printer', const='BreaklinePrinter')
    cmdArguments = argumentParser.parse_args()

    #instantiate CheatHandler
    chandler = CheatHandler(extention, directory)
    chandler.indexCheatsheets()
    chandler.parseRequestedCheatSheet(cmdArguments.cheatsheet)

    #instantiate CheatPrinter based on command-line argument.
    printer_type = cmdArguments.printer

    if printer_type is None:
        printer_type = 'InlinePrinter'

    printer_constructor = globals()[printer_type]
    cprinter = printer_constructor(chandler.getConfigParser())
    cprinter.printCheatSheet()

    #Everything is fine and we can exit with 0
    exit(0)

if __name__ == "__main__":
    main()
