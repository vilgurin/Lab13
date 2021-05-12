""" 
Representation of tic tac toe
https://github.com/stepansushko1/tic_tac_toe
"""
from btree import LinkedBinaryTree


class Board:
    """
    Represents the board
    """
    def init(self):
        self.board = []
        self.free_pos = []
        for i in range(3):
            lst = []
            for j in range(3):
                lst.append(" ")
                self.free_pos.append((i,j))
            self.board.append(lst)
        self.last_board = None

    def get_status(self):
        """
        Get the currents status of the board
        """
        if self.get_x_or_o(self.board,'x'):
            return 'x'
        elif self.get_x_or_o(self.board,"0"):
            return "0"
        elif not self.get_x_or_o(self.board,'x') and not\
        self.get_x_or_o(self.board,"0") and self.get_empty_space:
            return "continue"
        else:
            return "draw"


    def get_x_or_o(self,lst,par):
        """
        The additional function checks whether x or 0
        """
        if lst[0][0] == lst[0][1] and lst[0][1] == lst[0][2] and lst[0][0] == par or\
           lst[1][0] == lst[1][1] and lst[1][1] == lst[1][2] and lst[1][0] == par or\
           lst[2][0] == lst[2][1] and lst[2][1] == lst[2][2] and lst[2][0] == par or\
           lst[0][0] == lst[1][0] and lst[1][0] == lst[2][0] and lst[0][0] == par or\
           lst[0][1] == lst[1][1] and lst[1][1] == lst[2][1] and lst[0][1] == par or\
           lst[0][2] == lst[1][2] and lst[1][2] == lst[2][2] and lst[0][2] == par or\
           lst[0][0] == lst[1][1] and lst[1][1] == lst[2][2] and lst[0][0] == par or\
           lst[0][2] == lst[1][1] and lst[1][1] == lst[2][0] and lst[0][2] == par:

            return True
        return False

    def get_empty_space(self,lst):
        """
        Returns False if there is empty space in board, True otherwise
        """
        for i in lst:
            for j in i:
                if j == " ":
                    return False

        return True

    def make_move(self,position,turn):
        """
        Make user move
        """
        if turn != 'x' and turn != '0':
            raise IndexError
        try:
            self.board[position[0]][position[1]] = turn
        except IndexError:
            raise IndexError

    def make_computer_move(self):
        """ Make computer move"""
        pass

    def generate_random_move(self, board, turn):
        """
        Generate random move from pc
        """
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = turn
                    pos = (i,j)

                    return board,pos

    def build_tree(self):
        """
        Builds tree
        """
        combinations_tree = LinkedBinaryTree(self.board)
        counter = 0
        board = self.board

        def recurse_build(board):
            """
            Helper function
            """
            if self.get_status() == "x":
                return -1

            elif self.get_status() == "0":
                return 1

            elif self.get_status() == "draw":
                return 0

            else:

                if counter % 2 == 0:
                    turn = '0'
                else:
                    turn = "x"

                board_left = self.generate_random_move(board, turn)[0]
                board_right = self.generate_random_move(board_left, turn)[0]

                board_right = board_right[self.generate_random_move(board, turn)[1][0]][self.generate_random_move(board, turn)[1][1]] = ""


                combinations_tree.insert_left(board_left)
                combinations_tree.insert_right(board_right)

                recurse_build(board_left)
                recurse_build(board_right)

        counter += 1
        recurse_build(board)

        return combinations_tree



    def str(self):
        """
        Str method
        """
        output = ""
        for i in self.board:
            output += str(i) + '\n'
        return output[:-1]
