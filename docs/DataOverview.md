Overview of the data
====================

We provide a statistical overview of the Chaska, Minnesota dataset.

To generate the .json file from the .osm file, run the following:

    $ python maps/data.py './data/chaska-map.osm'

This will generate the following output file:

    data/chaska-map.osm.json

Size of the file
----------------
The original OSM file is 50.4 MB.  The JSON file generated from the OSM file is 55.8 MB.

Number of unique users
----------------------
177 users have edited this map.  Most are not included in the results below.

        $ python maps/users.py './data/chaska-map.osm'
        set(['42429',
             '503Greg',
             'AJ_LA',
                .
                .
                .
             'zdavkeos'])

Number of nodes and ways
------------------------
The Chaska map contains 235,838 nodes and 21,050 ways:

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

Number of chosen type of nodes, like cafes, shops, etc.
-------------------------------------------------------
