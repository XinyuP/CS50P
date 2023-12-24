"""

A binary file is a collection of ones and zeros. 

Binary file can store anything including music and image data

PIL: Python Imaging Library



Animated GIFs are a type if image file that has many image files within it 
that are played in sequence over and over again, creating a simplistic animation
or video effect

"""


import sys
from PIL import Image
images = []


for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)


images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=100, loop=0
)




































