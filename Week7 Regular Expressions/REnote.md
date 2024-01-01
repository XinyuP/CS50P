regular expression aka regexes

use pattern to match some data like user input

examine patterns in our code

define patterns in code to compare them against data that we receive from someone else

"""

```
. any charater except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions
{m,n} range m through n repetitions


```

raw strings are strings that don't format special characters
each character is taken at face-value

-> Placing an r in front of the strings
tells the python interpreter to treat the string as a raw string,
similar to how placing an f in front of a string tells the python interpreter to
treat as a format string

eg.
`\n` in a reguar string becomes a special newline character
`\n` in a raw string is just a single "\" and a single "n"

`.+`
is equivalent to
`..*`

`^` matches the "start" of the string
`$` matches the "end" of the string
just befire the newline at the end of the string

```




re.search(r"^.+[@].+\.edu$", email)




[] set of characters allowed
[^] complementing the set (set of characters not allowed)


if re.search(r"^[^@]+@[^@]+\.edu$", email)

^: match from the start
[^@]: "any char except @"
[^@]+: one or more "any char except @"

\.edu: followed by literally .edu

$: match at the end





[a-zA-Z0-9_]
replaced with \w



\w represents "word character"
which is commonly known as a alphanumeric symbol



In Python's re module, which is used for working with regular expressions,
\w is a special sequence that matches any alphanumeric character,
including letters, numbers, and underscores.

It's like a shortcut for matching common character types.

To break it down:

Alphanumeric characters:
These are your basic letters and numbers. So,
\w will match
    'a', 'b', 'c', ..., 'z',
    'A', 'B', 'C', ..., 'Z',
    '0', '1', '2', ..., '9'.
    Underscores: It also matches the underscore character ('_').




\d = [0-9]
\D = [^0-9]
\s = whitespace chars [ \t\r\n\f\v]
\S = not a whitespace char
\w = [a-zA-Z0-9_]
\W = [^a-zA-Z0-9_]

\b Matches the empty string, but only at the beginning or end of a word.
\B Matches the empty string, but only when it is not at the beginning or end of a word.

```

This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.

This means that r'py\B' matches 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'. \B is just the opposite of \b,

```

\s matches any whitespace character.
It includes space, tab(\t), newline (\n), carriage return (\r), form feed (\f), and vertical tab (\v).
So, it's more like [ \t\r\n\f\v].





if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email)

A|B either A or B

(...) a group

(?:...) non-capturing version


```

"""

```

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
(\w+\.)* 0 or more subdomain



********
re.match(pattern, string, flags=0)

Don't need to specify the ^ symbol at the beginning
re.match automatically start matching from the beginning

re.match("c", "abcdef")    # No match
re.search("c", "abcdef")   # Match


********
re.fullmatch(pattern, string, flags=0)

Don't need to specify the ^ or & symbol
check both the match at the start and end of string

re.fullmatch("p.*n", "python") # Match
re.fullmatch("r.*n", "python") # No match





Document:
re.match(pattern, string, flags=0)

If zero or more characters at the beginning of string match the regular expression pattern,
return a corresponding Match.

Return None if the string does not match the pattern;

note that this is different from a zero-length match.

Note that even in MULTILINE mode, re.match() will only match at the
beginning of the string and not at the beginning of each line.

If you want to locate a match anywhere in string, use search()
instead (see also search() vs. match()).




search() vs. match()
Python offers different primitive operations based on regular expressions:

re.search() checks for a match "anywhere" in the string (this is what Perl does by default)

re.match() checks for a match only at the "beginning" of the string

re.fullmatch() checks for "entire" string to be a match




Document:

re.fullmatch(pattern, string, flags=0)
If the whole string matches the regular expression pattern,
return a corresponding Match.

Return None if the string does not match the pattern;
note that this is different from a zero-length match.



"""

```

```


"""

Extracting info from user input


prompt user for the URL of their twitter profile

extract username from that URL


re.sub(pattern, repl, string, count=0, flags=0)

-> Cleaning up data and get rid of the data that we don't want


"""



"""
re.sub(pattern, repl, string, count=0, flags=0)

Return the string obtained by replacing the leftmost non-overlapping
occurrences of pattern in string by the replacement repl.
If the pattern isn't found, string is returned unchanged.

repl can be a string or a function; if it is a string,
any backslash escapes in it are processed.

That is, \n is converted to a single newline character,
\r is converted to a carriage return, and so forth.

Unknown escapes of ASCII letters are reserved for future use and treated as errors.
Other unknown escapes such as \& are left alone.
Backreferences, such as \6, are replaced with the substring matched by group 6
in the pattern.

"""

```

"""
re.split(pattern, string, maxsplit=0, flags=0)

Split string by the occurrences of pattern.

If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list.

If maxsplit is nonzero, at most maxsplit splits occur,
and the remainder of the string is returned as the final element of the list.

```
"""

Extracting info from user input

prompt user for the URL of their twitter profile

extract username from that URL


***** re.search(pattern, string, flags=0)


We only save the username in the backend if the input url actually
matched the proper pattern


using conditional way to solve the problem




"""

>>> re.split(r'\W+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split(r'(\W+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split(r'\W+', 'Words, words, words.', 1)
['Words', 'words, words.']
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']

```

If there are capturing groups in the separator and it matches at the start of the string, the result will start with an empty string. The same holds for the end of the string:

```
>>> re.split(r'(\W+)', '...words, words...')
['', '...', 'words', ', ', 'words', '...', '']

```

That way, separator components are always found at the same relative indices within the result list.

Empty matches for the pattern split the string only when not adjacent to a previous empty match.

```
>>> re.split(r'\b', 'Words, words, words.')
['', 'Words', ', ', 'words', ', ', 'words', '.']
>>> re.split(r'\W*', '...words...')
['', '', 'w', 'o', 'r', 'd', 's', '', '']
>>> re.split(r'(\W*)', '...words...')
['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']
```

"""

`re.findall(pattern, string, flags=0)`
Return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.

The result depends on the number of capturing groups in the pattern. If there are no groups, return a list of strings matching the whole pattern. If there is exactly one group, return a list of strings matching that group. If multiple groups are present, return a list of tuples of strings matching the groups. Non-capturing groups do not affect the form of the result.

```
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
[('width', '20'), ('height', '10')]

```
