from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        in_ext = os.path.splitext(sys.argv[1])[1].lower()
        out_ext = os.path.splitext(sys.argv[2])[1].lower()
        exts = {".jpg",".jpeg",".png"}
        if in_ext not in exts or out_ext not in exts:
            sys.exit("Invalid input")
        elif in_ext != out_ext:
            sys.exit("Input and output have different extensions")
        else:
            input_file_name = sys.argv[1]
            output_file_name = sys.argv[2]
            dress_up(input_file_name, output_file_name)



def dress_up(input_file_name, output_file_name):
    try:
        shirt_img = Image.open("shirt.png")
        with Image.open(input_file_name) as before_img:
        # before_img =  Image.open(input_file_name)
            fitted_before_img = ImageOps.fit(before_img, shirt_img.size)
            fitted_before_img.paste(shirt_img, shirt_img)
            fitted_before_img.save(output_file_name)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    
if __name__ == "__main__":
    main()

"""
the second use of shirt_img in the paste() method is for the purpose
of maintaining the transparency of the image being pasted. 

It uses the alpha channel of the image as a mask to determine how to 
blend the pixels with the background image.



wherein the first shirt represents the image to overlay and the second shirt represents 
a “mask” indicating which pixels in photo to update.




os.path.splitext(path)

split the path into a pair of (root, extension)



Split the pathname path into a pair (root, ext) such that root + ext == path, 
and the extension, ext, is empty or begins with a period and contains at most one period.

If the path contains no extension, ext will be '':

>>>
splitext('bar')
('bar', '')



If the path contains an extension, then ext will be set to this extension, 
including the leading period. Note that previous periods will be ignored:
>>>
splitext('foo.bar.exe')
('foo.bar', '.exe')

splitext('/foo/bar.exe')
('/foo/bar', '.exe')



Leading periods of the last component of the path are considered to be part of the root:
>>>
splitext('.cshrc')
('.cshrc', '')

splitext('/foo/....jpg')
('/foo/....jpg', '')


"""









# import sys
# from PIL import Image, ImageOps


# def main():
#     if len(sys.argv) < 3:
#         sys.exit("Too few command-line arguments")
#     elif len(sys.argv) > 3:
#         sys.exit("Too many command-line arguments")
#     elif sys.argv[1].split(".")[-1].lower() not in {"jpg","jpeg","png"} or sys.argv[2].split(".")[-1].lower() not in {"jpg","jpeg","png"} :
#         sys.exit("Invalid input")
#     elif sys.argv[1].split(".")[-1].lower() != sys.argv[2].split(".")[-1].lower():
#         sys.exit("Input and output have different extensions")
#     else:
#         input_file_name = sys.argv[1]
#         output_file_name = sys.argv[2]
#         dress_up(input_file_name, output_file_name)

# def dress_up(input_file_name, output_file_name):
#     try:
#         shirt_img = Image.open("shirt.png")
#         before_img =  Image.open(input_file_name)
#         before_before_img = ImageOps.fit(before_img, shirt_img.size)
#         before_before_img.paste(shirt_img, shirt_img)
#         before_before_img.save(output_file_name)

#     except FileNotFoundError:
#         sys.exit("Input does not exist")

    
# if __name__ == "__main__":
#     main()




















