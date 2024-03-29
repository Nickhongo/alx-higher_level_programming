#!/usr/bin/python3
"""
import sys
"""


import sys
import json
from pathlib import Path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

p = Path("add_item.json")

datalist = []

if p.exists():
    datalist += load_from_json_file(p)

    for i in range(1, len(sys.argv)):
        datalist.append(sys.argv[i])

    save_to_json_file(datalist, p)
else:
    for i in range(1, len(sys.argv)):
        datalist.append(sys.argv[i])
    save_to_json_file(datalist, p)
