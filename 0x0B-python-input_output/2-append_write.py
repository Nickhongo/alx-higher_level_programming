#!/usr/bin/python3
"""
 a function that appends a string at the end of a text file (UTF8)
 and returns the number of characters added
"""


def append_write(filename="", text=""):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(text)
            return len(text)
    except Exception as e:
        print(f"An error occured: {e}")
        return 0
