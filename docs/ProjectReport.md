Project Report
==============

Problems encountered in my map
------------------------------

The first problem I ran into was that it was hard using the OpenStreetMap site to select a region centered on my neighborhood that was not too large and not too small.

The second problem is that very few places of business in my town are very well-labelled in OpenStreetMap.  So it is hard to get information on how many cafes, shops, etc. there are.

Overview of the data
--------------------

We provide a statistical overview of the Chaska, Minnesota dataset.

To generate the .json file from the .osm file, run the following:

    $ python maps/data.py './data/chaska-map.osm'

This will generate the following output file:

    data/chaska-map.osm.json

First, we start up MongoDB:

    $ mongod --dbpath ~/data/db

Next, we import the data:

    $ mongoimport --db map --collection map --file ./data/chaska-map.osm.json

Now start mongo:

    $ mongo
    > use map
    switched to db map


### Size of the file

The original OSM file is 50.4 MB.  The JSON file generated from the OSM file is 55.8 MB.

Let's look at the size of the actual collection:

    > db.map.dataSize()
    71478400

You can see that it's about 71 MB.

### Number of unique users

212 users have edited this map.  
             
    > db.map.distinct("created.user").length
    212

### Number of nodes and ways

The Chaska map contains 235,838 nodes and 21,050 ways:

    > db.map.find( { type: "node" } ).length()
    235838
    
    > db.map.find( { type: "way" } ).length()
    21050

Other ideas about the datasets
------------------------------

Very few businesses in my map were labelled with their type of business.  It might be good to flag these.  But it would be very tedious and time-consuming to add the appropriate information to all of them.  I wonder whether it would be possible to programmatically get that data from the Google Maps API.  But using information from Google Maps to add information to OpenStreetMap seems like data stealing and might violate the terms of agreement for Google Maps.

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

I fixed this with changeset:

* [27809933](http://www.openstreetmap.org/changeset/27809933): Changed street from "Vierling" to "Vierling Drive East".
