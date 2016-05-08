#!/usr/bin/env python3


from configparser import ConfigParser
from io import StringIO
import os

import unittest
from unittest.mock import patch

from cheat.printer import *


class PrinterTest(unittest.TestCase):
    """Some basic tests to check the Printer classes"""

    def setUp(self):
        """
        Setting up the test by reading the test cheatsheet with expected content to test against.
        """

        self.cp = ConfigParser()
        directory = os.path.dirname(os.path.realpath(__file__))
        testfile = os.path.join(directory, "test.ini")
        self.cp.read(testfile)

    def test_PrinterFactory_InlinePrinter(self):
        """
        See if the PrinterFactory is giving us the objects we want.
        """

        self.assertIs(
            PrinterFactory.create_printer("InlinePrinter"),
            InlinePrinter
        )

    def test_PrinterFactory_BreaklinePrinter(self):
        """
        See if the PrinterFactory is giving us the objects we want.
        """

        self.assertIs(
            PrinterFactory.create_printer("BreaklinePrinter"),
            BreaklinePrinter
        )

    def test_PrinterFactory_NonsensePrinter(self):
        """
        See if PrinterFactory
        """

        # Using lambda turns our dictionary lookup into a callable.
        self.assertRaises(KeyError, lambda: PrinterFactory.create_printer("NonsensePrinter"))

    def test_InlinePrinter(self):
        """
        Testing if the InlinePrinter does its job.
        """

        #TODO Make this more readable
        expected_output = "test cheat a lorem\ntest cheat b ipsum\ntest cheat c dolor\n"
        printer = InlinePrinter(self.cp)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_InlinePrinter_width(self):
        """
        Test to see if the calculated width is correct.
        """
        printer = InlinePrinter(self.cp)
        self.assertEqual(printer.width, "12")

    def test_BreaklinePrinter(self):
        """
        Testing if the BreaklinePrinter does its job
        """

        #TODO Make this more readable
        expected_output = "test cheat a \n lorem\ntest cheat b \n ipsum\ntest cheat c \n dolor\n"
        printer = BreaklinePrinter(self.cp)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)


    def test_Printer_printsheet(self):
        """
        Testing if the printsheet for loop does its job
        """

        #TODO Make this more readable
        expected_output = "test cheat a\ntest cheat b\ntest cheat c\n"
        printer = Printer(self.cp)
        template = "{0}"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet(template)
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
