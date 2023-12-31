"""

Extracting info from user input

prompt user for the URL of their twitter profile

extract username from that URL


***** re.search(pattern, string, flags=0)


We only save the username in the backend if the input url actually 
matched the proper pattern


using conditional way to solve the problem




"""
import re

url = input("URL: ").strip()

# matches = re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
# if matches:
#     print(f"Username: {matches.group(3)}")


#### walrus operator := ####
# if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE): 
# if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE): # not everything is username, twitter username only allows [a-z0-9_]
if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # delete $, tolerate other stuff at the end of the url
    print(f"Username: {username.group(1)}")


# http://www.twitter.com/davidjmalan
# https://twitter.com/davidjmalan
# https://www.twitter.com/davidjmalan


# # non capturing in re.search()
# username = re.search(r"^https?://(www\.)?twitter\.com/", url) # Username: ('www.',)
# username = re.search(r"^https?://(www\.)?twitter\.com/(.*)", url) # Username: ('www.', 'davidjmalan')
# username = re.search(r"^https?://(?:www\.)?twitter\.com/(.*)", url) # Username: ('davidjmalan',)

# print(f"Username: {username}")



