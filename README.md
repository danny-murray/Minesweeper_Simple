# Simplified Minesweeper

A simple version of the game Minesweeper. The code enables the user to create their own grid and where to place the mines; and then play the game. 
Here's an overview of the code:

1. The `get_user_input` function prompts the user to enter the size of the grid (number of rows and columns). It validates the input and returns the dimensions as integers.

2. The `validate_cell` function is a helper function that validates whether a cell is a mine (`'#'`) or a clear spot (`'-'`). It returns `True` if the cell is valid, and `False` otherwise.

3. The `get_grid` function takes the grid dimensions as input and allows the user to input the mine placements for each cell. It ensures that the user enters a valid configuration and returns the constructed grid.

4. The `count_adjacent_mines` function calculates the number of adjacent mines for a given cell in the grid. It takes the grid, row, and column as input and returns the count of adjacent mines.

5. The `construct_grid` function creates a new grid based on the user-defined grid. It iterates over each cell and replaces the clear spots (`'-'`) with the count of adjacent mines. The resulting grid is returned.

6. The `print_grid` function prints the grid in a visually formatted manner, row by row.

7. The `play_minesweeper` function serves as the main entry point of the game. It welcomes the user and initializes the grid by obtaining the dimensions and constructing the grid. It then displays the constructed grid.

To play the game, run the `play_minesweeper` function, follow the prompts to set up the grid and place the mines, and observe the constructed grid with the mine counts.
