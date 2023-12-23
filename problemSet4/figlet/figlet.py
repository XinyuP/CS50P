# import sys

# import pyfiglet
# import random

# def main():
#     get_figlet_text()

# def get_figlet_text():
#     if len(sys.argv) == 0:
#         text = input("What's the text? ")
#         figlet_text = pyfiglet.figlet_format(text, font=f) 
#         print(figlet_text)
        
#     elif len(sys.argv) == 3:
#         if sys.argv[1] not in ["-f", "--font"]:
#             sys.exit("Invalid usage")

#         f = sys.argv[2]
#         try:
#             pyfiglet.Figlet(font=f)
        
#         except pyfiglet.FontNotFound:
#             sys.exit("Invalid usage")
    
#         text = input("What's the text? ")
#         figlet_text = pyfiglet.figlet_format(text, font=f) 
#         print(figlet_text)
        
#     else:
#         sys.exit("Invalid usage")
    


# if __name__ == "__main__":
#     main()

##############################################

# import sys
# from pyfiglet import Figlet
# import random

# def main():
#     get_figlet_text()

# def get_figlet_text():
#     figlet = Figlet()
#     font_list = figlet.getFonts()

#     if len(sys.argv) == 1:
#         text = input("What's the text? ")
#         f = random.choice(font_list)
#         figlet.setFont(font=f) 
#         print(figlet.renderText(text))
        
#     elif len(sys.argv) == 3:
#         if sys.argv[1] not in ["-f", "--font"]:
#             sys.exit("Invalid usage")

#         f = sys.argv[2]
#         if f not in font_list:
#             sys.exit("Invalid usage")
    
#         text = input("What's the text? ")
#         figlet.setFont(font=f)
#         print(figlet.renderText(text))
        
#     else:
#         sys.exit("Invalid usage")
    


# if __name__ == "__main__":
#     main()




# #############################################

# import sys
# from pyfiglet import Figlet
# import random

# def main():
#     get_figlet_text()

# def get_figlet_text():
#     figlet = Figlet()
#     font_list = figlet.getFonts()

#     if len(sys.argv) == 1:
#         f = random.choice(font_list)
#         figlet.setFont(font=f) 
        
#     elif len(sys.argv) == 3:
#         if sys.argv[1] not in ["-f", "--font"]:
#             sys.exit("Invalid usage")
#         f = sys.argv[2]
#         if f not in font_list:
#             sys.exit("Invalid usage")
#         figlet.setFont(font=f)

#     else:
#         sys.exit("Invalid usage")
    
#     text = input("What's the text? ")
#     print(figlet.renderText(text))



# if __name__ == "__main__":
#     main()





##############################################


import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
font_list = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        f = random.choice(font_list)
        figlet.setFont(font=f) 
        get_figlet_text("What's the text? ", f)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")

        f = sys.argv[2]
        if f not in font_list:
            sys.exit("Invalid usage")

        get_figlet_text("What's the text? ", f)

    else:
        sys.exit("Invalid usage")
    


def get_figlet_text(prompt, f):
    text = input(prompt)
    figlet.setFont(font=f)
    print(figlet.renderText(text))


if __name__ == "__main__":
    main()





































