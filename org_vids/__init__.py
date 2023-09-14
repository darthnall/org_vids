import os

def sort():
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
