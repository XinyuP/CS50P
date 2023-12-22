"""

Making my own library



bundle up the code you keep reusing 
and make your own python module or package

You can keep it local on your PC or cloud server

or 

you can bundle it up, make it free and open source, and put it on PyPI
for others to use as well

"""


def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__":
    main()  



"""

__name__

a special variable whose value is automatically set by python to be "__main__" 
when you run a file from the command line

"""




















