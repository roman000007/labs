class Game:

    def __init__(self):
        self.u1 = User(Board.X_CELL, "Roma")
        self.u2 = User(Board.O_CELL, "Max")
        self.b = Board()
        self.curr_user = self.u1

    def start(self):
        while self.b.check_winner():
            ok = False
            while not ok:
                print(self.curr_user.msg)
                row, col = [int(x) - 1 for x in input().split()]
                ok = self.b.put(self.curr_user.cell, row, col)
                if not ok:
                    print("Incorrect coordinates!")
            print(self.b)
            self.curr_user = self.u2 if self.curr_user == self.u1 else self.u1


class Board:
    ROWS = 3
    COLS = 3
    EMPTY_CELL = " "
    O_CELL = "O"
    X_CELL = "X"
    X_WINS = 3
    O_WINS = 4
    DRAW = 5

    def __init__(self):
        self.__field = []
        for i in range(Board.ROWS):
            tmp = []
            for j in range(Board.COLS):
                tmp.append(Board.EMPTY_CELL)
            self.__field.append(tmp)

    def put(self, turn, row, col):
        if row >= Board.ROWS or col >= Board.COLS:
            return False
        if self.__field[row][col] != Board.EMPTY_CELL:
            return False

        self.__field[row][col] = turn
        return True

    # TODO: fix
    def check_winner(self):
        for i in range(3):
            if self.__field[i][0] == self.__field[i][1] == self.__field[i][2] != Board.EMPTY_CELL:
                return Board.X_WINS if self.__field[i][0] == Board.X_CELL else Board.O_WINS

        for i in range(3):
            if self.__field[0][i] == self.__field[1][i] == self.__field[2][i] != Board.EMPTY_CELL:
                return Board.X_WINS if self.__field[0][i] == Board.X_CELL else Board.O_WINS

        if self.__field[0][0] == self.__field[1][1] == self.__field[2][2] != Board.EMPTY_CELL:
            return Board.X_WINS if self.__field[0][0] == Board.X_CELL else Board.O_WINS

        if self.__field[2][0] == self.__field[1][1] == self.__field[2][0] != Board.EMPTY_CELL:
            return Board.X_WINS if self.__field[2][0] == Board.X_CELL else Board.O_WINS
        return Board.DRAW

    def __str__(self):
        s = "-" * 3
        s += "\n"
        for rows in self.__field:
            for row in rows:
              s += row
            s += "\n"
        s += "-" * 3
        return s


class User:
    def __init__(self, cell, name):
        self.cell = cell
        self.name = name
        self.msg = self.name + " turn! Enter coordinates:"


if __name__ == "__main__":
    g = Game()
    g.start()


