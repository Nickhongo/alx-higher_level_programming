#!/usr/bin/python3

def text_indentation(text):
    """prints a text with 2 new lines after each of these characters"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ['.', '?', ':']:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
