

def main():
    faces = input()
    converted_faces = convert(faces)
    print(converted_faces)



def convert(s):
    return s.replace(":)", "🙂").replace(":(", "🙁")

main()