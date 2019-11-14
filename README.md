<p>
<img width="200" src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" align="right" >
</p>

# AirBnB clone - The console
------------
## Table of Contents
* [Description](#description)
* [Files](#files)
* [Requirements](#requirements)
* [Installation](#installation)
* [Compile](#compile)
* [Execute](#execute)
* [Example](#example)
* [Bugs](#bugs)
* [Authors](#authors)

## Description
The console of the AirBnB clone is a command interpreter to manage the AirBnB objects, that allow to undestand the manipulation of the information required and how is storage in the program.

## Files
- models: Module that contains all the classes .
  - engine
    - __init__.py: Files named __init__.py are used to mark directories on disk as Python package directories
    - file_storage.py: class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
  - __init__.py: Files named __init__.py are used to mark directories on disk as Python package directories.
  - amenity.py: Module that contains the Amenity class
  - base_model.py: Module that contains the BaseModel class
  - city.py: Module that contains the City class
  - place.py: Module that contains the Place class
  - review.py: Module that contains the Review class
  - state.py: Module that contains the State class
  - user.py: Module that contains the User class
- tests: Module that contains the tests.
  - test_models: Module that contains uniqtest
    - __init__.py: Files named __init__.py are used to mark directories on disk as Python package directories.
    - test_amenity.py: Module of the Amenity unittest
    - test_base_model.py: Module of the BaseModel unittest
    - test_city.py: Module of the City unittest
    - test_place.py: Module of the Place unittest
    - test_review.py: Module of the Review unittest
    - test_state.py: Module of the State unittest
    - test_user.py: Module of the User unittest
  - __init__.py: Files named __init__.py are used to mark directories on disk as Python package directories
- AUTHORS: File that contains all individuals having contributed content to the repository
- console.py: command interpreter (console.py) to have these commands

---
## Requirements
   - The console for AirBnb clone is designed for python3.4

## Installation
   - Clone this repository: `https://github.com/nickmoran06/AirBnB_clone.git"`

## Execute
   - Run the console in interactive mode: `./console`
   - But also in non-interactive mode: (like the Shell project in C:) echo "help" | `./console.py`

##Example
Run the executable in your terminal:
```
$ ./console
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  emptyline  help  quit  show  update

(hbnb) create BaseModel
58917d36-8ac0-40cf-856b-218ce2e1b533
(hbnb)
(hbnb) show BaseModel 58917d36-8ac0-40cf-856b-218ce2e1b533
[BaseModel] (58917d36-8ac0-40cf-856b-218ce2e1b533) {'updated_at': datetime.datetime(2019, 11, 14, 4, 1, 20, 385729), 'created_at': datetime.datetime(2019, 11, 14, 4, 1, 20, 385305), 'id': '58917d36-8ac0-40cf-856b-218ce2e1b533'}
(hbnb)
(hbnb) update BaseModel 58917d36-8ac0-40cf-856b-218ce2e1b533 first_name "Betty"
(hbnb)
(hbnb) all
[BaseModel] (58917d36-8ac0-40cf-856b-218ce2e1b533) {'first_name': 'Betty', 'id': '58917d36-8ac0-40cf-856b-218ce2e1b533', 'updated_at': datetime.datetime(2019, 11, 14, 4, 5, 16, 112168), 'created_at': datetime.datetime(2019, 11, 14, 4, 1, 20, 385305)}
(hbnb)
(hbnb) quit

```
---

## Bugs
There are no known bugs.

## Authors
[Diego Ramos](https://github.com/DiegoRmsR) | [@Imdiegoramoss](https://twitter.com/@Imdiegoramoss)

[Nicolás Morán](https://github.com/nickmoran06) | [@nickmoran06](https://twitter.com/nickmoran06)

