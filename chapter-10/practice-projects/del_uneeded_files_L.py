import os
from pathlib import Path


MAX_FILE_SIZE_IN_MB = 1
ONE_MB_IN_BYTES = 1000000
MAX_FILE_SIZE_IN_BYTES = MAX_FILE_SIZE_IN_MB * ONE_MB_IN_BYTES

for foldername, subfolders, filenames in os.walk(Path("del_uneeded_files")):
    print("\n" + "CURRENT FOLDER: " + foldername)

    for filename in filenames:
        file_path = Path(foldername) / filename
        file_size = os.path.getsize(file_path)
        if file_size > MAX_FILE_SIZE_IN_BYTES:
            print(os.path.abspath(file_path))
            print(filename + ": " + str(file_size) + " Bytes")
