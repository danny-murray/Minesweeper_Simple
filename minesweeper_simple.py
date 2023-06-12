''' Simplified Minesweeper '''

# Determining grid size
def get_user_input():
    print("Let's begin by setting up the size of your grid.")
    while True:
        rows = input("Number of rows: ")
        columns = input("Number of columns: ")
        print("Thank you.")
        if rows.isdigit() and columns.isdigit():
            return int(rows), int(columns)
        else:
            print("Sorry, that's an invalid input. Please only enter numbers for the grid dimensions.")

# Validation for mines and clear spots
def validate_cell(cell):
    return cell in ['#', '-']

# User designed grid
def get_grid(rows, columns):
    grid = []
    print(f"Now let's place the mines into your {rows}x{columns} grid.")
    print("# = mine, - = clear spot.")
    print("Separate the # and - with only a space.")
    print("Please do not enter any other characters.")

    for _ in range(rows):
        while True:
            row_input = input().split()
            if len(row_input) != columns or not all(validate_cell(cell) for cell in row_input):
                print(f"Sorry, that's an invalid input. Please only enter {columns} cells with '#' or '-'.")
            else:
                grid.append(row_input)
                break
    return grid

# Counting the mines
def count_adjacent_mines(grid, row, column):
    rows = len(grid)
    columns = len(grid[0])
    count = 0

    for r in range(max(0, row - 1), min(rows, row + 2)):
        for c in range(max(0, column - 1), min(columns, column + 2)):
            if grid[r][c] == '#':
                count += 1
    return count

# Creating the grid
def construct_grid(grid):
    rows = len(grid)
    columns = len(grid[0])
    constructed_grid = [[None for _ in range(columns)] for _ in range(rows)]

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '-':
                count = count_adjacent_mines(grid, row, column)
                constructed_grid[row][column] = str(count)
            else:
                constructed_grid[row][column] = grid[row][column]

    return constructed_grid

# Printing the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# The Game Setup
def play_minesweeper():
    print("Welcome to Dan's Simple Minesweeper!")

    rows, columns = get_user_input()
    grid = get_grid(rows, columns)
    constructed_grid = construct_grid(grid)

    print("Your constructed grid: ")
    print_grid(constructed_grid)

play_minesweeper()