table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def print_table(table):
    longest_word_lengths = determine_longest_word_length(table)

    WIDTH = len(table[0])
    HEIGHT = len(table)

    for x in range(WIDTH):
        for y in range(HEIGHT):
            padding = longest_word_lengths[y]
            padded_value = table[y][x].rjust(padding)
            print(padded_value, end=" ")
        print()


def determine_longest_word_length(table):
    longest_word_length = []

    for y in range(len(table)):
        result = max(table[y], key=len)
        longest_word_length.append(len(result))

    return longest_word_length


print_table(table_data)


# for index, column in enumerate(table_data):
#     for value in column:
#         print(value.rjust(longest_word_length[index]), end=' ')
#     print()

# for word_length, index in enumerate(longest_word_length):
#     for value in table_data:
#         print(column[].rjust(longest_word_length[]), end=' ')


# for x in range(WIDTH):
#     for alist in table_data:
#         print(alist[x].rjust(longest_word_length[0]), end=' ')
#     print()

# for y in range(HEIGHT):
#     for v in table_data[y][0:WIDTH]:
#         print(v.rjust(longest_word_length[0]))


# column = []

# for x in range(WIDTH):
#     for y in range(HEIGHT):
#         column.append(table_data[y][x])
