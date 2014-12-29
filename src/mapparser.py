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

def count_tags(filename):
        tags = {}
        for (event, node) in ET.iterparse(filename, ['start']):
            tag = node.tag
            if tag and not tag in tags.keys():
                tags[tag] = 0
            tags[tag] = tags[tag] + 1
        return tags

def test():

    tags = count_tags('../test-data/mapparser-example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}



if __name__ == "__main__":
    test()