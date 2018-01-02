#!/usr/bin/env python3


"""
Main script, where all parts come together.
containers Argument Parser for commandline arguments and main function.
"""


from argparse import ArgumentParser
from configparser import ConfigParser
from configparser import Error as ConfigParserError
from os import path
from printer import PrinterFactory
from utils import print_available_sheets, Colors


def commandline():
    """
    Configures the Argument Parser and returns the parsed commandline args.
    """

    description = 'Cool Command-line Cheatsheets'
    help_general = 'The cheatsheet you want to see'
    help_list = 'List all available cheatsheets'
    help_colors = 'Print output without colors'
    help_inline = 'One cheat per line, this is the default'
    help_breakline = 'Break lines'

    argumentparser = ArgumentParser(description=description)
    printertype = argumentparser.add_mutually_exclusive_group()

    argumentparser.add_argument('--list', dest='listcheats', action="store_true", required=False, help=help_list)
    argumentparser.add_argument('--nc', dest='nocolor', action="store_false", required=False, help=help_colors)
    argumentparser.add_argument('cheatsheet', nargs='?', help=help_general)

    printertype.set_defaults(printer='InlinePrinter')
    printertype.add_argument('-l', help=help_inline, action='store_const', dest='printer', const='InlinePrinter')
    printertype.add_argument('-b', help=help_breakline, action='store_const', dest='printer', const='BreaklinePrinter')

    return argumentparser


def main(argparser):
    """
    Where the magic happens.

    :param argparser: Configures Argument Parser
    """

    cmdargs = argparser.parse_args()
    filedir = path.dirname(path.abspath(__file__ + '../../'))
    cheatsheetdir = path.join(filedir, 'cheatsheets/')
    extension = '.ini'
    filename = cheatsheetdir + str(cmdargs.cheatsheet) + extension

    # Lists the Cheatsheats
    if cmdargs.listcheats:
        print_available_sheets(cheatsheetdir)
        exit(0)

    # Print help if nothing is provided
    if cmdargs.cheatsheet is None:
        argparser.print_help()
        exit(2)

    # Check if file is available
    if not path.isfile(filename):
        print(filename + ' is not available.')
        exit(2)

    # Build the Printer
    configparser = ConfigParser()
    printer_constructor = PrinterFactory.create_printer(cmdargs.printer)
    printcolored = cmdargs.nocolor
    cheatprinter = printer_constructor(configparser, Colors, printcolored)

    # Read the file and exit script
    try:
        configparser.read(filename)
        cheatprinter.printsheet()
        exitcode = 0
    except ConfigParserError as exception:
        print(filename + ' contains error.\n')
        print(exception)
        exitcode = 1
    finally:
        exit(exitcode)

if __name__ == '__main__':

    ARGPARSER = commandline()
    main(ARGPARSER)
