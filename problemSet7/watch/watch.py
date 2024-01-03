import re
import sys

"""

http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0


https://youtu.be/xvFZjo5PgG0



Note that * and + are “greedy,” insofar as “they match as much text as possible,” p
er docs.python.org/3/library/re.html#regular-expression-syntax. 

Adding ? immediately after either, a la *? or +?, 
“makes it perform the match in non-greedy or minimal fashion; 
as few characters as possible will be matched.”



"""


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # if url := re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\".*$", s):
    if url := re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(.+?)\".*$", s):

        return f"https://youtu.be/{url.group(1)}"
    return None




if __name__ == "__main__":
    main()



    