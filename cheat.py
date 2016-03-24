#!/usr/bin/python3
import configparser
import argparse
from sys import path
from sys import exit
from os import listdir

class Printer:

    def __init__(self, configparser):
        self.configparser = configparser

    def printCheatSheet(self):
        raise NotImplementedError

class InlinePrinter(Printer):
    """
    Prints the cheatssheet inline, so that it's grep-able.
    """

    @property
    def width(self):
        width = 10
        
        for description in self.configparser['cheats']:
            if len(description) > width:
                width = len(description)

        return width

    def printCheatSheet(self):
        for description in self.configparser['cheats']:
            value = self.configparser['cheats'][description]
            output = "{0:<{1}} {2}".format(description, self.width, value)

            print(output)

class BreaklinePrinter(Printer):
    """
    Prints the cheatsheet with newlines
    """

    def printCheatSheet(self):
        for description in self.configparser['cheats']:
            value = self.configparser['cheats'][description]
            output = "{0} \n {1}".format(description, value)

            print(output)

def main():
    directory = path[0] + "/config/"
    extention = ".ini"
    description = "Cool Command-line Cheatsheets"
    help_general = "The cheatsheet you want to see"
    help_inline = "One cheat per line, this is default"
    help_breakline = "Break lines"
    parser = configparser.ConfigParser()

    #COMMAND-LINE ARGUMENTS!
    argumentParser = argparse.ArgumentParser(description=description)
    argumentParser.add_argument('cheatsheet', help=help_general)
    group = argumentParser.add_mutually_exclusive_group()
    group.add_argument('-l', help=help_inline, action='store_const', dest='printer', const='InlinePrinter')
    group.add_argument('-b', help=help_breakline, action='store_const', dest='printer', const='BreaklinePrinter')
    cmd_arguments = argumentParser.parse_args()

    if cmd_arguments.printer is None:
        CheatPrinterConstructor = globals()['InlinePrinter']
    else:
        CheatPrinterConstructor = globals()[cmd_arguments.printer]

    filename = directory + cmd_arguments.cheatsheet + extention

    try:
        parser.read(filename)
        cheatPrinter = CheatPrinterConstructor(parser)
        cheatPrinter.printCheatSheet()
    except configparser.Error as exception:
        print(exception)
    except:
        print(filename + " not available or contains errors")

    exit(0)

if __name__ == "__main__":
    main()
