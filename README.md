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

maps.users.process_map Results
------------------------------
177 users have edited this map.  Most are not included in the results below.

        $ python maps/users.py './data/chaska-map.osm'
        set(['42429',
             '503Greg',
             'AJ_LA',
                .
                .
                .
             'zdavkeos'])

maps.audit.audit Results
------------------------------
Note the first problem found: OpenStreetMaps gives a street named "Vierling".  It is actually called "Vierling Drive".

        $ python maps/audit.py './data/chaska-map.osm'
        {'101': set(['County Road 101']),
         '44': set(['County Road 44']),
         '62': set(['CR 62']),
         'Ave': set(['17th Ave',
                     'Downing Ave',
                     'King Ave',
                     'Philipp Ave',
                     'Queen Ave']),
         'Blvd': set(['8280 Market Blvd',
                      'Crossroads Blvd',
                      'Eagle Creek Blvd',
                      'Market Blvd',
                      'Tasha Blvd']),
         'Circle': set(['Dakota Circle']),
         'Ct': set(['Brittany Ct', 'Cattail Ct', 'Dublin Ct', 'Wyndam Ct']),
         'Dr': set(['Marsh Dr', 'Omega Dr', 'Philipp Dr', 'Wyndam Dr']),
         'East': set(['10th Avenue East',
                      '12th Avenue East',
                      '1st Ave East',
                      'Lake Drive East',
                      'Vierling Drive East']),
         'Ln': set(['Coneflower Ln', 'Skyview Ln', 'Warbler Ln']),
         'Spur': set(['Cheyenne Spur', 'Erie Spur']),
         'St': set(['Balinese St', 'N Pine St']),
         'Vierling': set(['Vierling']),
         'Way': set(['Philipp Way', 'Wagner Way'])}
        Traceback (most recent call last):
          File "maps/audit.py", line 78, in <module>
            run(sys.argv[1])
          File "maps/audit.py", line 70, in run
            better_name = update_name(name, mapping)
          File "maps/audit.py", line 58, in update_name
            better_street_type = mapping[m.group()]
        KeyError: 'Vierling'
