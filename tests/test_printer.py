#!/usr/bin/env python3

import sys
sys.path.append('../cheat/')
import printer


import unittest


class PrinterTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_Printer(self):
        assert True


if __name__ == '__main__':
    unittest.main()
