Overview of the data
====================

Student provides a statistical overview about their chosen dataset, like:
* size of the file
* number of unique users
* number of nodes and ways
* number of chosen type of nodes, like cafes, shops etc

To generate the .json file from the .osm file, run the following:

    $ python maps/data.py './data/chaska-map.osm'

This will generate the following output file:

    data/chaska-map.osm.json
