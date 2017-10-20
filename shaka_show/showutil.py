"""
Common utility functions used in Shaka-Show web app
"""

import argparse
import importlib


def load_handlers(name):
    """Return a tuple containing the URL and the URL's handler.
    Each handler should be contained in a file called handlers.py.
    These modules contain each handler and are retrrieved with "default_handlers".
    """
    handler_module = importlib.import_module(name)
    return handler_module.default_handlers


def parse_args():
    """
    Function takes in arguments from a command line.
    If the argument is preceded by '-p' or '--port', the value for the source file's port number is changed from '8888' to the argument value.
    One of the input arguments is the source file; if the argument is empty or if the source file does not exist, return error.
    Function returns a dictionary of the port number, the file name, and the source code of the source file.
    """

    # parse the input
    parser = argparse.ArgumentParser()

    # optionally check for a port number input; if no input, default port number to 8888
    parser.add_argument("-p", "--port", help="assigns the port number", default="8888")

    # Check for source file input; if no input, return error
    parser.add_argument("file", help="reads in the source file name")

    # Assign parsed components to 'args'
    args = parser.parse_args()

    # Open source file and append each line of code to a list
    source = None
    with open(args.file, "r") as f:
        source = f.read()

    # Create a dictionary containing the 'port number,' the 'file name,' and the 'source code' of the source file
    newdict = {'port': args.port, 'filename': args.file, 'source': source}

    # return the dictionary value
    return newdict
