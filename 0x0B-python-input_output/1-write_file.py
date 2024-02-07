#!/usr/bin/python3
"""
This function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"An error occured: {e}")
        return 0
