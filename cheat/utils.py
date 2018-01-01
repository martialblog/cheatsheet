#!/usr/bin/env python3


"""
Utility functions and classes for common tasks.
"""


from configparser import ConfigParser
from configparser import Error as ConfigParserError
from os import listdir, path


def print_available_sheets(directory):
    """
    Prints all available cheatsheets in the sheet folder to the stdout.

    :param directory: The directory where the cheatsheets are located.
    """

    parser = ConfigParser()
    files = listdir(directory)

    for name in sorted(files):
        try:
            parser.read(path.join(directory, name))
            print('{0}'.format(parser['main']['name']))
        except ConfigParserError:
            # TOOD: What to do here?
            pass


class Colors:
    """
    Wrapper class for colored output
    """

    DEFAULT = '\033[94m'
    PARAM = '\033[93m'
    RESET = '\033[1;m'
