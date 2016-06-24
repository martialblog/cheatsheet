#!/usr/bin/env python3


import os
import unittest


class MainTest(unittest.TestCase):
    """
    Tests for the main script
    TODO: I'm sure there must be a better way.
    """

    def setUp(self):
        """
        Defining the exitcodes

        Expected Exitcodes:
        On Unix, the return value is the exit status of the
        process encoded in the format specified for wait()
        https://docs.python.org/3.5/library/os.html#os.system
        """

        self.exit_0 = 0 << 8
        self.exit_1 = 1 << 8
        self.exit_2 = 2 << 8

    def test_main_success(self):
        """
        Lazy testing of the main function.
        Checks the exitcode if everythings runs as planed.
        """

        command = '/usr/bin/env python3 cheat/cheat.py git > /dev/null'
        status = os.system(command)

        self.assertEqual(status, self.exit_0)

    def test_main_failure_no_cheatsheet(self):
        """
        Lazy testing of the main function.
        Checks the exitcode if the cheathsheet isn't available.
        """

        command = '/usr/bin/env python3 cheat/cheat.py not_available > /dev/null 2>&1'
        result = os.system(command)

        self.assertEqual(result, self.exit_1)

    def test_main_failure_no_argument(self):
        """
        Lazy testing of the main function.
        Checks the exitcode if there is no argument passed.
        """

        command = '/usr/bin/python3 cheat/cheat.py > /dev/null 2>&1'
        result = os.system(command)

        self.assertEqual(result, self.exit_2)
