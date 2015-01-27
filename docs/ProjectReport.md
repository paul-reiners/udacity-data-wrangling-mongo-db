Project Report
==============

Problems encountered in my map
------------------------------

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
