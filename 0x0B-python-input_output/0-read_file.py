#!/usr/bin/python3
"""
The function read_file - reads a text file (UTF-8) and prints
it to stdout
"""


def read_file(filename=""):
    """
    reads a text file and prints it to stdout
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")
