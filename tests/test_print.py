#!/usr/bin/env python3


from configparser import ConfigParser
from io import StringIO
import os
import unittest
from unittest.mock import patch

import cheat.printer as cp
import cheat.utils as u


class PrinterTest(unittest.TestCase):
    """
    Some basic tests to check the Printer classes.
    """

    def setUp(self):
        """
        Setting up the test by reading the test-cheatsheet
        with expected content to test against.
        """

        directory = os.path.dirname(os.path.realpath(__file__))
        testfile = os.path.join(directory, "testsheets", "test.ini")
        self.cparser = ConfigParser()
        self.cparser.read(testfile)

    def test_PrinterFactory_InlinePrinter(self):
        """
        See if the PrinterFactory is giving us the objects we want.
        """

        self.assertIs(
            cp.PrinterFactory.create_printer("InlinePrinter"),
            cp.InlinePrinter
        )

    def test_PrinterFactory_BreaklinePrinter(self):
        """
        See if the PrinterFactory is giving us the objects we want.
        """

        self.assertIs(
            cp.PrinterFactory.create_printer("BreaklinePrinter"),
            cp.BreaklinePrinter
        )

    def test_PrinterFactory_NonsensePrinter(self):
        """
        See if the PrinterFactory fails when it's supposed to.
        I guess this isn't that useful...
        """

        # Using lambda turns our dictionary lookup into a callable.
        self.assertRaises(KeyError, lambda: cp.PrinterFactory.create_printer("NonsensePrinter"))

    def test_InlinePrinter_colored(self):
        """
        Testing if the InlinePrinter does its job.
        """

        # Done this way for better readablility.
        lines = ["Test cheat a \x1b[94mlorem\x1b[1;m\n",
                 "Test cheat b \x1b[94mipsum\x1b[1;m\n",
                 "Test cheat c \x1b[94mdolor\x1b[1;m\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.InlinePrinter(self.cparser, u.Colors, print_colored=True)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)


    def Test_InlinePrinter(self):
        """
        Testing if the InlinePrinter does its job.
        """

        # Done this way for better readablility.
        lines = ["Test cheat a lorem\n",
                 "Test cheat b ipsum\n",
                 "Test cheat c dolor\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.InlinePrinter(self.cparser, u.Colors, print_colored=False)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_InlinePrinter_width(self):
        """
        Test to see if the calculated width is correct.
        """

        printer = cp.InlinePrinter(self.cparser, u.Colors, print_colored=False)

        expected_length = str(len('Test Cheat A'))
        self.assertEqual(printer.width, expected_length)

    def test_BreaklinePrinter(self):
        """
        Testing if the BreaklinePrinter does its job.
        """

        # Done this way for better readablility.
        lines = ["Test cheat a \n lorem\n",
                 "Test cheat b \n ipsum\n",
                 "Test cheat c \n dolor\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.BreaklinePrinter(self.cparser, u.Colors, print_colored=False)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_Printer_printsheet(self):
        """
        Testing if the printsheet for loop does its job.
        """

        # Done this way for better readablility.
        lines = ["Test cheat a\n",
                 "Test cheat b\n",
                 "Test cheat c\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.Printer(self.cparser, u.Colors)
        template = "{0}"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printcheats(template)
            self.assertEqual(fake_out.getvalue(), expected_output)
