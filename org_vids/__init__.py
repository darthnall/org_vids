import os

def sort():
<<<<<<< HEAD
    client_name = input("""
        Input new filename for files.\n
        Files are formatted as follows:\n

        <NEW_FILENAME>-<INDEX>.<EXTENSION>\n\n

        New Filename: """)
    files = os.listdir("./org_vids/input")
    for index, file in enumerate(files):
        ext = file.split(".")[1]
        new_name = f"{client_name}-{index}.{ext}"
        os.rename(os.path.abspath(f"./org_vids/input/{file}"), os.path.abspath(f"./org_vids/output/{new_name}"))
=======
    new_filename = input("The new files will appear as:\nNew name, hyphen, number\n\nNew filename: ")
    files = os.listdir("./org_vids/input")
    for index, file in enumerate(files):
        ext = files[0].split(".")[1]
        new_filename = f"{new_filename}-{index}.{ext}"
        os.rename(f"./org_vids/input/{file}", f"./org_vids/output/{new_filename}")
>>>>>>> fc393c272fcac221443a22a336a502d2b0d93792
