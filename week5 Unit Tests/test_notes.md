# write code to test your code

### assert

- if True, nothing happen

- if False, error on the screen

### AssertionError

try except

### pytest

unit testing is a formal way of describing testing individual units of your program (functions)

unit tests are typically tests for functions that you have written

### organizing tests into multiple files, even a folder

`__init__.py`

even if this file is empty,

this file has an effect of telling python to treat that folder as not just a module, but a package

a package is a python module or multiple modules that are organized inside of a folder

`__init__.py` file is just a visual indicator to Python that indeed it should treat that folder as a package

if we had more code in this folder, we could do more thing with `__init__.py` file, but for now, it is just a clue that it's indeed meant to be a package and not just a module or file alone
