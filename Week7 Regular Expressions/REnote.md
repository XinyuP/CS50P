regular expression aka regexes

use pattern to match some data like user input

examine patterns in our code

define patterns in code to compare them against data that we receive from someone else

"""
. any charater except a newline

- 0 or more repetitions

* 1 or more repetitions
  ? 0 or 1 repetition
  {m} m repetitions
  {m,n} range m through n repetitions

raw strings are strings that don't format special characters
each character is taken at face-value

-> Placing an r in front of the strings
tells the python interpreter to treat the string as a raw string,
similar to how placing an f in front of a string tells the python interpreter to
treat as a format string

eg.
\n in a reguar string becomes a special newline character
\n in a raw string is just a single "\" and a single "n"

.+
is equivalent to
..\*

^ matches the "start" of the string

$ matches the "end" of the string
just befire the newline at the end of the string

"""

"""

Case Sensitivity

re.search(pattern, string, flags=0)

flags:
re.IGNORECASE
re.MULTILINE
re.DOTALL

Scan through string looking for the first location where the regular expression
pattern produces a match, and return a corresponding Match.

Return None if no position in the string matches the pattern;

note that this is different from finding a zero-length match at some point in the string.

(\w+\.)? 0 or 1 subdomain
(\w+\.)\* 0 or more subdomain

"""
