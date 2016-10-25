#!/usr/bin/env python3


import os
import utils as u
from argparse import ArgumentParser
from configparser import ConfigParser
from printer import PrinterFactory
from sys import exit


def commandline():

    description = "Cool Command-line Cheatsheets"
    help_general = "The cheatsheet you want to see"
    help_list = "List all available Cheatsheets"
    help_colors = "Print output without colors"
    help_inline = "One cheat per line, this is default"
    help_breakline = "Break lines"

    argumentparser = ArgumentParser(description=description)
    printertype = argumentparser.add_mutually_exclusive_group()

    argumentparser.add_argument('--list', dest='listcheats', action="store_true", required=False, help=help_list)
    argumentparser.add_argument('--nc', dest='nocolor', action="store_false", required=False, help=help_colors)
    argumentparser.add_argument('cheatsheet', nargs='?', help=help_general)

    printertype.set_defaults(printer='InlinePrinter')
    printertype.add_argument('-l', help=help_inline, action='store_const', dest='printer', const='InlinePrinter')
    printertype.add_argument('-b', help=help_breakline, action='store_const', dest='printer', const='BreaklinePrinter')

    cmd_arguments = argumentparser.parse_args()

    if cmd_arguments.listcheats:
        u.print_available_sheets(cheats_directory)
        exit(0)

    if cmd_arguments.cheatsheet is None:
        argumentparser.print_help()
        exit(2)

    return cmd_arguments


def main(cmd_args):

    extension = ".ini"
    filename = cheats_directory + cmd_args.cheatsheet + extension

    configparser = ConfigParser()
    CheatPrinterConstructor = PrinterFactory.create_printer(cmd_args.printer)
    colors = u.colors
    printcolored = cmd_args.nocolor

    cheatprinter = CheatPrinterConstructor(configparser, colors, printcolored)

    try:
        configparser.read(filename)
        cheatprinter.printsheet()
        exitcode = 0
    except Exception as e:
        # I know lazy handling... Sorry.
        # TOOD better exception handling.
        print(filename + " not available or contains errors.")
        print(e)
        exitcode = 1
    finally:
        exit(exitcode)


if __name__ == "__main__":

    cheats_filedir = os.path.dirname(os.path.realpath(__file__))
    cheats_directory = os.path.join(cheats_filedir, "sheets/")

    args = commandline()
    main(args)
