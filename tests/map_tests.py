from nose.tools import *
import pprint
import maps.mapparser
import maps.tags
import maps.users
import maps.audit

OSMFILE = "./test-data/audit-example.osm"

def test_mappparser_count_tags():
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

def test__tags_process_map():
    keys = maps.tags.process_map('./test-data/tags-example.osm')
    pprint.pprint(keys)
    assert keys == {'lower': 5, 'lower_colon': 0, 'other': 2, 'problemchars': 0}

def test_users_process_map():
    users = maps.users.process_map('./test-data/users-example.osm')
    pprint.pprint(users)
    assert len(users) == 4

def test_audit_audit():
    st_types = maps.audit.audit(OSMFILE)
    assert len(st_types) == 3
    pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = maps.audit.update_name(name, maps.audit.mapping)
            print name, "=>", better_name
            if name == "West Lexington St.":
                assert better_name == "West Lexington Street"
            if name == "Baldwin Rd.":
                assert better_name == "Baldwin Road"
