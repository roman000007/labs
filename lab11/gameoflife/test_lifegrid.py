# Program for playing the game of Life.
from gameoflife.lifegrid import LifeGrid

# Define the initial configuration of live cells.
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]

# Set the size of the grid.
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Indicate the number of generations.
NUM_GENS = 8


def main():
    # Constructs the game grid and configure it.
    h = int(input("Enter height of grid: "))
    w = int(input("Enter width of grid: "))
    num_gens = int(input("Enter number of generations: "))
    grid = LifeGrid(w, h)
    grid.configure(INIT_CONFIG)

    # Plays the game.
    draw(grid)
    for i in range(num_gens):
        evolve(grid)
        draw(grid)


# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    live_cells = []

    # Iterate over the elements of the grid.
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):

            # Determine the number of live neighbors for this cell.
            neighbors = grid.num_live_neighbors(i, j)

            # Add the (i,j) tuple to liveCells if this cell contains
            # a live organism in the next generation.
            if (neighbors == 2 and grid.is_live_cell(i, j)) or (neighbors == 3):
                live_cells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(live_cells)


# Prints a text based representation of the game grid.
def draw(grid):
    print(str(grid))


# Executes the main routine.
main()
