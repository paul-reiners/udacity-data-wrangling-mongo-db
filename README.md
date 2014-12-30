udacity-data-wrangling-mongo-db
===============================

Udacity Data Wrangling with MongoDB course work

For information on project structure, see [<i>Learn Python the Hard Way</i>](http://learnpythonthehardway.org/book/ex46.html).

maps.mapparser.count_tags Results
------------------
    $ python mapparser.py '../data/chaska-map.osm'
    {'bounds': 1,
     'member': 2957,
     'meta': 1,
     'nd': 263583,
     'node': 235838,
     'note': 1,
     'osm': 1,
     'relation': 93,
     'tag': 86417,
     'way': 21050}

maps.tags.process_map Results
------------------
    $ python maps/tags.py './data/chaska-map.osm'
    {'lower': 40146, 'lower_colon': 44211, 'other': 2060, 'problemchars': 0}
