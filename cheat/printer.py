#!/usr/bin/env/python3


class Printer:
    """
    Base class for the cheatsheet printers. Takes care of the actuall printing.

    Args:
    Takes a configparser objects to print.
    """

    def __init__(self, configparser):
        self.configparser = configparser

    def printsheet(self, template):
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
        width = len(max(self.configparser['cheats'], key=len))

        return str(width)

    def printsheet(self):
        print_format = "{0:<" + self.width + "} {1}"
        super().printsheet(print_format)


class BreaklinePrinter(Printer):
    """
    Prints the cheatsheet and breaks the line after the description.
    """

    # TODO Maybe use ljust rjust
    def printsheet(self):
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
        return PrinterFactory.printer_classes[name]
