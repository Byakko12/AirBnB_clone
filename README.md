# AirBnB_clone
![AirBnB](https://drive.google.com/uc?export=view&id=11YSb1Q1uCtVta-UWQk0R--Ds2GXiwCTP)
## Description

This project is the first step to build a AirBnB, in this we can see 
the build in python a command line interface, for managing data and classes 
for storage data.

## How to install
copy link of repository and use de command `git clone` + link

`$ git clone https://github.com/Byakko12/AirBnB_clone.git`


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

## Examples of use

    (hbnb) all MyModel
    ** class doesn't exist **

    (hbnb) show BaseModel
    ** instance id missing **

    (hbnb) show BaseModel My_First_Model
    ** no instance found **

    (hbnb) create BaseModel
    49faff9a-6318-451f-87b6-910505c55907

    (hbnb) all BaseModel
    ["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

    (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
    [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

    (hbnb) destroy
    ** class name missing **

    (hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

    (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
    [BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

    (hbnb) create BaseModel
    2dd6ef5c-467c-4f82-9521-a772ea7d84e9

    (hbnb) all BaseModel
    ["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

    (hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

    (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
    ** no instance found **

    (hbnb) 

## The console

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

![firs step](https://drive.google.com/uc?export=view&id=1RVFLseW3BE5eaGQKOAVaHrKyX0kHvlKt)

## Tests

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

    $ python3 unittest -m discover tests
    Alternatively, you can specify a single test file to run at a time:

    $ python3 unittest -m tests/test_console.py

### Example of unittests
    guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
    ...................................................................................
    ...................................................................................
    .......................
    ----------------------------------------------------------------------
    Ran 189 tests in 13.135s

    OK
    guillaume@ubuntu:~/AirBnB$

# Authors
- **Juan David Latorre** [Github](https://github.com/Byakko12)