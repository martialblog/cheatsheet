#!/usr/bin/env python3


from io import StringIO
import os
import unittest
from unittest.mock import patch

import cheat.utils as u


class UtilTest(unittest.TestCase):
    """
    Tests for the util fucntions
    """

    def setUp(self):
        """
        Setting up the test by reading the test-cheatsheet
        with expected content to test against.
        """

        self.directory = os.path.dirname(os.path.realpath(__file__))


    def test_print_available_sheets(self):
        """
        Test of the print all cheatsheets function
        """

        expected_output = " unittest\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            u.print_available_sheets(self.directory)
            self.assertEqual(fake_out.getvalue(), expected_output)


    def test_colors(self):
        """
        Test of the color class
        """

        expected_output = "\033[94m"
        output = u.colors.DEFAULT

        self.assertEqual(output, expected_output)
