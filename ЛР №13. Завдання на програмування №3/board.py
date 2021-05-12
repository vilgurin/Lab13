from pprint import pprint
from btree import LinkedBinaryTree
from btnode import Node
import random
class Board:

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.tree = LinkedBinaryTree(self.board)
        # self.current = Board(self.board)

    def __str__(self):
        output = ""
        for i in self.board:
            output += str(i)+"\n"
        return output[:-1]


    def win_combination(self):

        for i in range(len(self.board)):
            for j in range(len(self.board)):

                    if self.board[i][j] == self.board[i][j-1]\
                         and self.board[i][j] == self.board[i][j-2]:
                        if self.board[i][j] == "x":
                            return 1
                        return 0

                    elif self.board[i][j] == self.board[i-1][j]\
                         and self.board[i][j] == self.board[i-2][j]:
                        if self.board[i][j] == "x":
                            return 1
                        return 0

                    elif self.board[i][j] == self.board[i-1][j-1]\
                         and self.board[i][j] == self.board[i-2][j-2]:
                        if self.board[i][j] == "x":
                            return 1
                        return 0
        return False


    def get_status(self):
        if self.get_status() == 1:
            return "x"

        elif self.get_status() == 0:
            return "0"

        elif self.get_status() == False:
            for row in self.board:
                for j in row:
                    if row[j] == "":
                        return "continue"
        else:
            return "draw"

    def make_move(self,position,turn):

        if turn != "x" and turn != "0":
            raise IndexError

        if self.board[position[0]][position[1]] == " ":
            try:
                self.board[position[0]][position[1]] = turn
            except IndexError:
                raise IndexError 
        else:
            raise IndexError

        
 


    # def build_tree(self):
    #     win_counter = 0
    #     counter = 0
        
    #     # board = self.board
        
    #     def build_tree1(board,counter):
    #         value = ""
    #         counter += 1
    #         last_position = 0

    #         if self.get_status() == "x":
    #             return 1

    #         elif self.get_status() == "0":
    #             # counter += 1
    #             return -1

    #         elif board.get_status() == "draw":
    #             return 0

    #         board1 = board
            
    #         if counter % 2 == 1:
    #             value = "0"
    #         else:
    #             value = "x"


    #         for i in range(len(board)):
    #             for j in range(len(board)):
    #                 if board[i][j] != "''":
    #                     board1[i][j] = value
    #                     last_position = (i,j)
    #                     break
    #         print(board1)

    #         board2 = board1

    #         for i in range(len(board2)):
    #             for j in range(len(board2)):
    #                 if board2[i][j] != "''":
    #                     board2[i[0]][i[1]] = value
    #                     board1[last_position[0],last_position[1]]
    #                     break
    #         print(board2)

    #         return max(build_tree1(board1,counter),build_tree1(board2,counter))

    #     return build_tree1(self.board,counter)



a = Board()
a.make_move((1,1),("x"))
a.make_move((1,1),("0"))
print(a)