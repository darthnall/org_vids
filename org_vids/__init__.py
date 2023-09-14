import os

def sort():
    client_name = input("Client name: ")
    files = os.listdir("./org_vids/input")
    for index, file in enumerate(files):
        ext = files[0].split(".")[1]
        new_filename = f"{client_name}-{index}.{ext}"
        os.rename(f"./org_vids/input/{file}", f"./org_vids/output/{new_filename}")
