import os

def sort():
    client_name = input("Client name: ")
    files = os.listdir("./input")
    for file in files:
        ext = file.split(".")[1]
        new_name = f"{client_name}-{file.index}.{ext}"
        os.rename(os.path.abspath(file), os.path.abspath(f".output/{new_name}"))
