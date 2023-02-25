import shutil, os, re
from pathlib import Path

extension_search_pattern = re.compile(r"^(.*)(\.txt)$")

# should i add the ability to change???
# dir_to_create = "text_files"
# path_to_copy_from = "../selective_copy"
# if Path(dir_to_create) == False:
#     os.mkdir(Path.cwd() / dir_to_create)


for foldername, subfolders, filenames in os.walk(Path("selective_copy")):
    for filename in filenames:
        match_object = extension_search_pattern.search(filename)
        if match_object != None:
            shutil.copy(Path(foldername) / filename, "text_files")
            print(match_object.group())
            print(filename)
            print(Path.cwd() / f"{foldername}\{filename}")
