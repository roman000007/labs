from arrays import Array2D

class LifeGrid:
    """
    Implements the LifeGrid ADT for use with the Game of Life.
    """
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1
    neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, num_rows, num_cols):
        """
        Creates the game grid and initializes the cells to dead.

        :param num_rows: the number of rows.
        :param num_cols: the number of columns.
        """
        # Allocates the 2D array for the grid.
        self._grid = Array2D(num_rows, num_cols)
        # Clears the grid and set all cells to dead.
        self.configure(list())

    def __str__(self):
        s = ""
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                s += str(self._grid[(i, j)]) + " "
            s += "\n"
        s+= "----------"
        return s

    def num_rows(self):
        """
        Returns the number of rows in the grid.

        :return: the number rows in the grid.
        """
        return self._grid.num_rows()

    def num_cols(self):
        """
        Returns the number of columns in the grid.

        :return:Returns the number of columns in the grid. 
        """
        return self._grid.num_cols()

    def configure(self, coord_list):
        """
        Configures the grid to contain the given live cells.
        
        :param coord_list: 
        :return: 
        """
        self._grid.clear(self.DEAD_CELL)
        for i, j in coord_list:
            self.set_cell(i, j)



    def is_live_cell(self, row, col):
        """
        Does the indicated cell contain a live organism?
        
        :param row: row of the cell.
        :param col: column of the cell.
        :return: the result of check.
        """
        return self._grid[(row,col)] == self.LIVE_CELL


    def clear_cell(self, row, col):
        """
        Clears the indicated cell by setting it to dead.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row,col)] = self.DEAD_CELL


    def set_cell(self, row, col):
        """
        Sets the indicated cell to be alive.

        :param row: row of the cell.
        :param col: column of the cell.
        """
        self._grid[(row,col)] = self.LIVE_CELL


    def num_live_neighbors(self, row, col):
        """
        Returns the number of live neighbors for the given cell.

        :param row: row of the cell.
        :param col: column of the cell.
        :return: 
        """
        count = 0
        for row_plus, col_plus in self.neighbours:
            if 0 <= row_plus + row < self.num_rows() and 0 <= col_plus + col < self.num_cols():
                if self.is_live_cell(row_plus + row, col_plus + col):
                    count += 1
        return count
