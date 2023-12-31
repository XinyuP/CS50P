"""

Extracting info from user input


prompt user for the URL of their twitter profile

extract username from that URL


re.sub(pattern, repl, string, count=0, flags=0)

-> Cleaning up data and get rid of the data that we don't want 


"""
import re

url = input("URL: ").strip()
# print(url)
# username = url.replace("https://twitter.com/", "")
# username = url.removeprefix("https://twitter.com/")

# username = re.sub(r"^https://twitter\.com/", "", url)
# username = re.sub(r"^https?://twitter\.com/", "", url)
# username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

print(f"Username: {username}")





# # non capturing in re.search()
# username = re.search(r"^https?://(www\.)?twitter\.com/", url) # Username: ('www.',)
# username = re.search(r"^https?://(www\.)?twitter\.com/(.*)", url) # Username: ('www.', 'davidjmalan')
# username = re.search(r"^https?://(?:www\.)?twitter\.com/(.*)", url) # Username: ('davidjmalan',)

# print(f"Username: {username}")





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