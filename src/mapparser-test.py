import unittest
import pprint
import mapparser

class TestMapParser(unittest.TestCase):

    def test_count_tags(self):
        tags = mapparser.count_tags('../test-data/mapparser-example.osm')
        pprint.pprint(tags)
        self.assertEqual(
            {'bounds': 1,
                'member': 3,
                'nd': 4,
                'node': 20,
                'osm': 1,
                'relation': 1,
                'tag': 7,
                'way': 1},
                tags)

if __name__ == '__main__':
    unittest.main()
