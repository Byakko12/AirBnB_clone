# AirBnB_clone

## Description

This project is the first step to build a AirBnB, in this we can see 
the build in python a command line interface, for managing data and classes 
for storage data.

## Execution

Your shell should work like this in interactive mode:

    
    $ ./console.py
    (hbnb) help
        
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $
    
But also in non-interactive mode: (like the Shell project in C)


    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $
    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $

### The console
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220307%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220307T043835Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=00eb6854b04fe5755726408feaa513db7796978459c87dc824145de83a48b2d7)

## Tests

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

    $ python3 unittest -m discover tests
    Alternatively, you can specify a single test file to run at a time:

    $ python3 unittest -m tests/test_console.py
# Authors
- **Juan David Latorre** [Github](https://github.com/Byakko12)