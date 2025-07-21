#! /urs/bin/env python3

__author__ = "fela14"
__author_email__ = "k.fakeye@yahoo.com"
__copyright__ = "Copyright (c) 2016 Chevron Nigeria"
__license__ = "MIT"

import sys

def doubler(number):
    # Give a number, double it and return the value
    result = number * 2
    return result

# Entry point for program
if __name__ == "__main__":
    # Retrieve command line input
    try:
        input = float(sys.argv[1])
    except (IndexError, ValueError) as e:
        # Indicate no command line parameter was provided
        print("You must provide a number as a parameter to this script")
        print("Example: ")
        print("  python example1.py 12")
        sys.exit(1)

    # Double the provided number and print output
    answer = doubler(input)
    print(answer)
