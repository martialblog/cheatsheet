#!/usr/bin/env python3


import os
from configparser import ConfigParser


def print_available_sheets(directory):
    """
    Prints all available cheatsheets in the sheet folder to the stdout.
    :param directory: The directory where the cheatsheets are located
    """

    cp = ConfigParser()

    for root, dirs, files in os.walk(directory):
        for name in files:
            cp.read(os.path.join(root, name))
            output = " {0}".format(cp['main']['name'])

            print(output)
