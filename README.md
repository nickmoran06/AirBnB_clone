<p>
<img width="200" src="https://lh4.googleusercontent.com/yUzaviDgzDIq4-ZHp9k0YU5fsz0nOdekNRt1qHgp7Qdlw5BNfe6bETEf5ZWd-Vkn_m57BPx7HcDrwFK41ptLnQLTNipWmTAtiQwZL_8s97Nkzn94xP7XVKb3RnV0fx8QEZoxlkVd" align="right" >
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
AirBnB clone - The console is 

## Files
File | Description
--- | ---
`shell.h` | header file
`main.` | Execute shell_loop.c
`shell_loop.c` | funtion tha wait for a string a process it.
`shell_read.c` | Function that obtains and reads a line
`shell_token.c` | Funtion tha tokenizes the string using two points as delimiters.
`shell_status.c` | Function that executes the processes
`shell_path.c` | Function related to executing commands
`shell_prosses` | function that creates a new process
`shelil_buitlings` | Funtion thet execute buitlings
`puts_grid.c` | Funtion tha print a matrix
`str_funt`.c | contains different functions for the handling of strings
`man_1_simple_shell` | Manual page for the simple_shell

---
## Requirements

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

