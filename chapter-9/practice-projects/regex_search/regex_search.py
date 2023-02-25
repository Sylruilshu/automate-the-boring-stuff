from pathlib import Path
import re

search_pattern = re.compile(r"foobar", re.IGNORECASE)

text_files_dir_path = Path("text_files")

print(text_files_dir_path.absolute())

file_paths = list(text_files_dir_path.glob("*.txt"))

# for file_path in file_paths:
#     file = open(file_path, 'r')
#     file_contents = file.read()
#     # print(file_contents)
#     match_object = search_pattern.search(file_contents)
#     if match_object != None:
#         print(match_object.group())
#         print(file_contents)
#     file.close()

for file_path in file_paths:
    file = open(file_path, "r")
    file_lines = file.readlines()
    for line in file_lines:
        # print(file_contents)
        match_object = search_pattern.search(line)
        if match_object != None:
            print(match_object.group())
            print(line.strip())
    file.close()
