#!/usr/bin/env/python3

class Printer:
    """
    Base class for the cheatsheet printers. Takes care of the actuall printing.
    """

    def __init__(self, configparser, print_colored=True):
        """
        BaseClass constucter.

        :param configparser: ConfigParser object with the cheatsheets.
        :param print_colored: Print console output with color or not.
        """

        self.configparser = configparser
        self.print_colored = print_colored

    def add_color(self, string):
        """
        Adds color to the console output.
        """

        CMD_BLUE = '\033[94m'
        CMD_YELLOW = '\033[93m'
        CMD_RESET = '\033[1;m'

        string = string.replace('<', CMD_YELLOW + '<')
        string = string.replace('>', '>' + CMD_RESET)

        colored = CMD_BLUE + string + CMD_RESET

        return colored

    def printsheet(self, template):
        """
        Loops over the entries in the ConfigParser and prints them with a specific template.

        :param template: Template to use with the format() function.
        """

        for description in self.configparser['cheats']:
            value = self.configparser['cheats'][description]
            value = self.add_color(value) if self.print_colored else value
            output = template.format(description, value)

            print(output)


class InlinePrinter(Printer):
    """
    Prints the cheatssheet line-by-line, so that it's grep-able.
    """

    @property
    def width(self):
        """
        Width of the longest ConfigParser entry.
        """

        width = len(max(self.configparser['cheats'], key=len))

        return str(width)

    def printsheet(self):
        """
        Sets the printer template to print inline and calls the Printer.printsheet().
        """

        print_format = "{0:<" + self.width + "} {1}"
        super().printsheet(print_format)


class BreaklinePrinter(Printer):
    """
    Prints the cheatsheet and breaks the line after the description.
    """

    def printsheet(self):
        """
        Sets the printer template to print with newlines and calls the Printer.printsheet().
        """

        print_format = "{0} \n {1}"
        super().printsheet(print_format)


class PrinterFactory:
    """
    Creates a Printer object from the String given by the argparse option.
    """

    printer_classes = {
        "InlinePrinter": InlinePrinter,
        "BreaklinePrinter": BreaklinePrinter
    }

    @staticmethod
    def create_printer(name):
        """
        Returns a specific Printer Object.

        :param name: Printer Object to return.
        """

        return PrinterFactory.printer_classes[name]
