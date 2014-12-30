from nose.tools import *
import unittest
import pprint
import maps.mapparser

def setup(self):
    print "SETUP!"

def teardown(self):
    print "TEAR DOWN!"

def test_count_tags():
    tags = maps.mapparser.count_tags('./test-data/mapparser-example.osm')
    pprint.pprint(tags)
    assert {'bounds': 1,
            'member': 3,
            'nd': 4,
            'node': 20,
            'osm': 1,
            'relation': 1,
            'tag': 7,
            'way': 1} == tags
