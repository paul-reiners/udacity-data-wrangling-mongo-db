#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Uses iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output is a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.
"""
import xml.etree.ElementTree as ET
import pprint
import sys

def count_tags(filename):
        tags = {}
        for (event, node) in ET.iterparse(filename, ['start']):
            tag = node.tag
            if tag and not tag in tags.keys():
                tags[tag] = 0
            tags[tag] = tags[tag] + 1
        return tags

def run(file_name):
    tags = count_tags(file_name)
    pprint.pprint(tags)

if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print "Usage: python mapparser.py input-file"
    else:
        run(sys.argv[1])
