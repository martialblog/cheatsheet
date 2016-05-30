#!/usr/bin/env/python3


class Printer:
    """
    Base class for the cheatsheet printers. Takes care of the actuall printing.
    """

    def __init__(self, configparser):
        """
        BaseClass constucter.

        :param configparser: ConfigParser object with the cheatsheets.
        """

        self.configparser = configparser

    def printsheet(self, template):
        """
        Loops over the entries in the ConfigParser and prints them with a specific template.

        :param template: Template to use with the format() function.
        """

        for description in self.configparser['cheats']:
            value = self.configparser['cheats'][description]
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
