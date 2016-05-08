#!/usr/bin/env python3


import sys
sys.path.append('../cheat/')

from configparser import ConfigParser
from io import StringIO

import unittest
from unittest.mock import patch

# Printer Classes that will be tested
from printer import *


class PrinterTest(unittest.TestCase):
    """Some basic tests to check the Printer classes"""

    def setUp(self):
        """
        Setting up the test by reading the test cheatsheet with expected content to test against.
        """

        self.cp = ConfigParser()
        self.cp.read("test.ini")

    #TODO Test if the width calculation is alright
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
