import os, shutil
from pathlib import Path


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]


# 1 TODO: find all given files with the prefix (.txt).
files_to_sort = Path("filling_in_gaps")
print(files_to_sort.absolute())

last_numbers_of_file_stems = []
file_stems_without_last_char = []
filenames = []
suffix = ".txt"

for filename in files_to_sort.glob(f"*{suffix}"):
    filenames.append(filename.name)
    filename_without_suffix = filename.stem
    file_stems_without_last_char.append(filename_without_suffix[:-1])
    last_char = filename_without_suffix[-1]
    last_numbers_of_file_stems.append(int(last_char))


# 2 TODO: locate any gaps in the numbering.
numbers_to_add = find_missing(last_numbers_of_file_stems)

for i in range(len(numbers_to_add)):
    last_numbers_of_file_stems.append(numbers_to_add[i])

last_numbers_of_file_stems.sort()
last_numbers_of_file_stems.pop(-(len(numbers_to_add)))

# 3 TODO: rename all files to close the gap.
last_numbers_of_new_file_stems = list(map(str, last_numbers_of_file_stems))

for i in range(len(last_numbers_of_new_file_stems)):
    shutil.copy(
        f"filling_in_gaps/{filenames[i]}",
        f"filling_in_gaps_renamed/{file_stems_without_last_char[i]}{last_numbers_of_new_file_stems[i]}{suffix}",
    )
