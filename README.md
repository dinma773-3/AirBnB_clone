## 0x00. AirBnB clone - The console
### Learning Objectives for this project: be able to explain to anyone, without the help of Google;
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is (*args*) and how to use it
What is (**kwargs**) and how to use it
How to handle named arguments in a function

### Execution
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

#### Testing:
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

### Authors:
Osaivbie Iguagbonmwen\n
[GitHub](https://github.com/Pintinz)\n
[Email](mailto:osaivbieiguagbonmwen@gmail.com)\n
Godsfavour Chukwudi\n
[GitHub](https://github.com/dinma773-3)\n
[Email](mailto:godsfavourchukwudi21@gmail.com)
