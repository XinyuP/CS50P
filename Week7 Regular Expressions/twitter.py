"""

Extracting info from user input


prompt user for the URL of their twitter profile

extract username from that URL


"""
url = input("URL: ").strip()
# print(url)

username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")

print(f"Username: {username}")









