#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

"""
Created on Thur 16:13 2022
@author: Nana Kauffmann
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    newlst = load_from_json_file("add_item.json")
    print(newlst)
except ValueError:
    newlst = []
for i in sys.argv[1:]:
    newlst.append(i)
save_to_json_file(newlst, "add_item.json")
