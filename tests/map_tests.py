from nose.tools import *
import pprint
import maps.mapparser
import maps.tags

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

def test_process_map():
    keys = maps.tags.process_map('./test-data/tags-example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}
