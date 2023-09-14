import os

def sort():
    new_filename = input("The new files will appear as:\nNew name, hyphen, number\n\nNew filename: ")
    files = os.listdir("./org_vids/input")
    for index, file in enumerate(files):
        ext = files[0].split(".")[1]
        new_filename = f"{new_filename}-{index}.{ext}"
        os.rename(f"./org_vids/input/{file}", f"./org_vids/output/{new_filename}")
