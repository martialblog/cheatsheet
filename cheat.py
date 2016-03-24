#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

#Lot or reduntant code here... gotta clean that up
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
    cmd_arguments = argumentParser.parse_args()

    parser = configparser.ConfigParser()
    filename = directory + cmd_arguments.cheatsheet + extention

    try:
        parser.read(filename)
    except configparser.Error as exception:
        print(exception)

    #instantiate CheatPrinter based on command-line argument.
    printer_type = cmd_arguments.printer

    if printer_type is None:
        printer_type = 'InlinePrinter'

    #Clener way of doing this?
    printer_constructor = globals()[printer_type]
    cprinter = printer_constructor(parser)
    cprinter.printCheatSheet()

    exit(0)

if __name__ == "__main__":
    main()
