from nose.tools import *
import pprint
import maps.mapparser
import maps.tags
import maps.users
import maps.audit
import maps.data

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

def test_data_process_map():
    data = maps.data.process_map('./test-data/data-example.osm', True)

    assert data[0] == {
                        "id": "261114295",
                        "visible": "true",
                        "type": "node",
                        "pos": [
                          41.9730791,
                          -87.6866303
                        ],
                        "created": {
                          "changeset": "11129782",
                          "user": "bbmiller",
                          "version": "7",
                          "uid": "451048",
                          "timestamp": "2012-03-28T18:31:23Z"
                        }
                      }
    assert data[-1]["address"] == {
                                    "street": "West Lexington St.",
                                    "housenumber": "1412"
                                      }
    assert data[-1]["node_refs"] == [ "2199822281", "2199822390",  "2199822392", "2199822369",
                                    "2199822370", "2199822284", "2199822281"]
