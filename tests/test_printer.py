#!/usr/bin/env python3


from configparser import ConfigParser
from io import StringIO
import os
import unittest
from unittest.mock import patch

import cheat.printer as cp


class PrinterTest(unittest.TestCase):
    """Some basic tests to check the Printer classes"""

    def setUp(self):
        """
        Setting up the test by reading the test cheatsheet with expected content to test against.
        """

        directory = os.path.dirname(os.path.realpath(__file__))
        testfile = os.path.join(directory, "test.ini")
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
        See if PrinterFactory
        """

        # Using lambda turns our dictionary lookup into a callable.
        self.assertRaises(KeyError, lambda: cp.PrinterFactory.create_printer("NonsensePrinter"))

    def test_InlinePrinter(self):
        """
        Testing if the InlinePrinter does its job.
        """

        # Done this way for better readablility.
        lines = ["test cheat a lorem\n",
                 "test cheat b ipsum\n",
                 "test cheat c dolor\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.InlinePrinter(self.cparser)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_InlinePrinter_width(self):
        """
        Test to see if the calculated width is correct.
        """

        printer = cp.InlinePrinter(self.cparser)

        expected_length = str(len('Test Cheat A'))
        self.assertEqual(printer.width, expected_length)

    def test_BreaklinePrinter(self):
        """
        Testing if the BreaklinePrinter does its job
        """

        # Done this way for better readablility.
        lines = ["test cheat a \n lorem\n",
                 "test cheat b \n ipsum\n",
                 "test cheat c \n dolor\n"]

        expected_output = lines[0] + lines[1] + lines[2]

        printer = cp.BreaklinePrinter(self.cparser)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_Printer_printsheet(self):
        """
        Testing if the printsheet for loop does its job.
        """

        # Done this way for better readablility.
        lines = ["test cheat a\n",
                 "test cheat b\n",
                 "test cheat c\n"]

        expected_output = lines[0] + lines[1] + lines[2]
        printer = cp.Printer(self.cparser)
        template = "{0}"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            printer.printsheet(template)
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_main(self):
        """
        Lazy testing of the main function. Checks if the exitcode is zero.
        """

        command = '/usr/bin/env python3 cheat/cheat.py git > /dev/null 2>&1'
        result = os.system(command)

        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
