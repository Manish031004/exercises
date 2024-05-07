class Board:
    def __init__(self, columns, rows):
        self.__columns = columns
        self.__rows = rows
        self.__initialize_board()

    def __initialize_board(self):
        self.__board = []
        for r in range(0, self.__rows):
            row = []
            for c in range(0, self.__columns):
                row.append(" ")
            self.__board.append(row)

    def print_board(self):
        self.__print_numbers()
        self.__print_line()
        for row in self.__board:
            self.__print_row(row)
            print("printing board")

    def __print_numbers(self):
        line = " "
        for c in range(1, self.__columns + 1):
            if c < 10:
                line += f" {c} "
            else:
                line += f" {c} "

    def __print_line(self):
        line = " "
        line += "_" * (self.__columns * 4 - 1)
        line += " "
        print(line)

    def __print_row(self, row):
        line = "|"
        for c in range(0, self.__column):
            line += f" {row[c] } |"
        print(line)
        self.__print_line()

    def check_column(self, column):

        for r in range(self.__rows - 1, -1, -1):
            if self.__board[r][column] == " ":
                return r
        return -1

    def add_token(self, column, row, token):
        self.__board[row][column] = token
        
    def is_valid_column(self, column):
        return 0<= 
