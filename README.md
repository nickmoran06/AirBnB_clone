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
`main.c` | Execute shell_loop.c
`shell_loop.c` | funtion tha wait for a string a process it.
`shell_read.c` | Function that obtains and reads a line
`shell_token.c` | Funtion tha tokenizes the string using two points as delimiters.
`shell_status.c` | Function that executes the processes
`shell_path.c` | Function related to executing commands
`shell_prosses` | function that creates a new process
`shell_buitlings` | Funtion thet execute buitlings
`puts_grid.c` | Funtion tha print a matrix
`str_funt`.c | contains different functions for the handling of strings
`man_1_simple_shell` | Manual page for the simple_shell

---
## Requirements
 * Simple_shell is designed to run on the Ubuntu 14.04 LTS Linux environment.
 * Must be compiled using the GNU v. gcc 4.8.4 compiler collection with flags-Wall, -Werror, -Wextra, and -pedantic.

## Installation
   - Clone this repository: `git clone "https://github.com/julgachancipa/simple_shell.git"`

## Compile
   - `gcc -Wall -Werror -Wextra -pedantic *.c -o hsh`

## Execute
   - Run the shell in interactive mode: `./hsh`
   - Or run the shell in non-interactive mode: `echo "pwd" | ./hsh`

## Example
Run the executable in your terminal after compiling:
```
$ ./hsh
$ # This is our rendition of the shell
$ ls -la
total 96
```
---

## Bugs
There are no known bugs.

## Authors
[Diego Ramos](https://github.com/DiegoRmsR) | [@Imdiegoramoss](https://twitter.com/Imdiegoramoss)

[Emma Gachancipa](https://github.com/julgachancipa) | [@julgachancipa](https://twitter.com/julgachancipa)

