import os, shutil
from pathlib import Path


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


# 1 TODO: find all given files with the prefix (.txt).
files_to_sort = Path("filling_in_gaps")
print(files_to_sort.absolute())

last_numbers_of_file_stems = []
file_stems_without_last_char = []
file_names = []
suffix = ".txt"

for filename in files_to_sort.glob(f"*{suffix}"):
    file_names.append(filename.name)
    file_name_without_suffix = filename.stem
    file_stems_without_last_char.append(file_name_without_suffix[:-1])
    print(file_name_without_suffix)
    last_char = file_name_without_suffix[-1]
    last_numbers_of_file_stems.append(int(last_char))
    print(last_char)

# 2 TODO: locate any gaps in the numbering.
print(file_names)
print(file_stems_without_last_char)
print(last_numbers_of_file_stems)

numbers_to_add = find_missing(last_numbers_of_file_stems)
print(numbers_to_add)

for i in range(len(numbers_to_add)):
    last_numbers_of_file_stems.append(numbers_to_add[i])

last_numbers_of_file_stems.sort()
print(last_numbers_of_file_stems)
last_numbers_of_file_stems.pop(-(len(numbers_to_add)))
print(last_numbers_of_file_stems)

# 3 TODO: rename all files to close the gap.
last_numbers_of_new_file_stems = list(map(str, last_numbers_of_file_stems))
print(last_numbers_of_new_file_stems)

for i in range(len(last_numbers_of_new_file_stems)):
    shutil.copy(
        f"filling_in_gaps/{file_names[i]}",
        f"filling_in_gaps_renamed/{file_stems_without_last_char[i]}{last_numbers_of_new_file_stems[i]}{suffix}",
    )
