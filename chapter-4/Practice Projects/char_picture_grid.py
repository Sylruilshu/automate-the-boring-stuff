grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['X', '.', '.', '.', '.', '.']]

WIDTH = 6
HEIGHT = 9

for x in range(WIDTH):
    row = []
    for y in reversed(range(HEIGHT)):
        row.append(grid[y][x]) 
    row_string = ''.join(row)
    print(row_string)