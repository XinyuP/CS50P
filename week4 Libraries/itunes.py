"""

** API: Applicaton Programming Interface

third-party services we can write code that talk to 

many APIs live on the internet these days 

API allows you to connect to the code of others 

we can write code that pretends to be a browser connects to that third-party API on a server
and download some data that we can them incorporate into our own program 


** requests

requests library allows you to make web request/internet request using python code 
as though you were a brower yourself

we can automate the retrieval of URLs that starts with http or https

https://pypi.org/project/requests/



** JSON 
JavaScript Object Notation

light weight data interchange format 

language agnostic format for exchanging data between computers

we can use any language to read or write python 

text-based format 


** json library

json comes with python



"""

import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit()

# Make HTTP request using Python to the server
# just like typing URLs into a browser and hit Enter
response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

# print(type(response)) # <class 'requests.models.Response'>
# print(response) # <Response [200]>
# print(type(response.json())) # <class 'dict'> 

# print(response.json())
# # The output of the json() method is a Python dictionary (or list) that represents the JSON data contained in the response. 

# print(json.dumps(response.json(), indent=2)) # serialize python object(dict, list, etc) to str (JSON-formatted string)



# Get the json object and convert to a Python dict
response_dict = response.json() # convert JSON to dict


for result in response_dict["results"]:
    print(result["trackName"])
    































