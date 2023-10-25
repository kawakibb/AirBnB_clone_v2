<p align="center">
  <img src="https://github.com/Adeniyii/AirBnB_clone/blob/main/assets/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

---

## Description :label:

The ALX-Holberton B&B is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This team project is part of the (Alx) Holberton School Software Engineering program. </br>
It represents the first step towards building a full web application.

This first step consists of:
- a custom command-line interface for data management,
- and the base classes for the storage of this data.

## Usage 💻

The console works both in interactive mode and non-interactive mode, much like a Unix shell.
It prints a prompt **(hbnb)** and waits for the user for input.

Command | Example
------- | -------
Run the console | ```./console.py```
Quit the console | ```(hbnb) quit```
Display the help for a command | ```(hbnb) help <command>```
Create an object (prints its id)| ```(hbnb) create <class>```
Show an object | ```(hbnb) show <class> <id>``` or ```(hbnb) <class>.show(<id>)```
Destroy an object | ```(hbnb) destroy <class> <id>``` or ```(hbnb) <class>.destroy(<id>)```
Show all objects, or all instances of a class | ```(hbnb) all``` or ```(hbnb) all <class>```
Update an attribute of an object | ```(hbnb) update <class> <id> <attribute name> "<attribute value>"``` or ```(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")```

<center><h3 id="1">Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ------ |
| 0: Authors/README File | [AUTHORS](./AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant|
| 2: Unit Testing | [/tests](./tests) | All class-defining modules are unittested |
| 3. Make BaseModel | [/models/base\_model.py](./models/base_model.py) | Defines a parent class to be inherited by all model classes|
| 4. Update BaseModel w/ kwargs | [/models/base\_model.py](./models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation|
| 5. Create FileStorage class | [/models/engine/file\_storage.py](./models/engine/file_storage.py) [/models/\_\_init\_\_.py](./models/__init__.py) [/models/base\_model.py](./models/base_model.py) | Defines a class to manage persistent file storage system|
| 6. Console 0.0.1 | [console.py](./console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7. Console 0.1 | [console.py](./console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8. Create User class | [console.py](./console.py) [/models/engine/file\_storage.py](./models/engine/file_storage.py) [/models/user.py](./models/user.py) | Dynamically implements a user class |
| 9. More Classes | [/models/user.py](./models/user.py) [/models/place.py](./models/place.py) [/models/city.py](./models/city.py) [/models/amenity.py](./models/amenity.py) [/models/state.py](./models/state.py) [/models/review.py](./models/review.py) | Dynamically implements more classes |
| 10. Console 1.0 | [console.py](./console.py) [/models/engine/file\_storage.py](./models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all  classes update file storage |
<br>
<br>

### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

### Non-interactive mode (example)

```bash
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
```

## Testing :straight_ruler:

Unittests for the ALX-Holberton B&B project are defined in the [tests](./tests)
folder. To run the entire test suite simultaneously, execute the following command:

```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time
