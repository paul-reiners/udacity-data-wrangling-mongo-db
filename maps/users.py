#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import pprint
import re
import sys
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    user = element.attrib['user']

    return user


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        if element.tag == "node":
            users.add(get_user(element))

    return users


def run(filename):
    users = process_map(filename)
    pprint.pprint(users)


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print "Usage: python maps/users.py input-file"
    else:
        run(sys.argv[1])
