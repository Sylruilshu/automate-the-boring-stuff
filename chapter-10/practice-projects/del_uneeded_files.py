import os
from pathlib import Path


for foldername, subfolders, filenames in os.walk(Path("del_uneeded_files")):
    print("\n" + "CURRENT FOLDER: " + foldername)

    for filename in filenames:
        file_path = Path(foldername) / filename
        file_size = os.path.getsize(file_path)
        if file_size > 1000000:
            print(os.path.abspath(file_path))
            print(filename + ": " + str(file_size) + " Bytes")
