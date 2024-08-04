# Backtracking - follows brute force approach[DFS] and tries to get multiple solutions to the given problem.
# abc(Permutations of a given tree)  =  3!  =  6

# 1. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def solve(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    #if board is empty
                    if board[i][j] == ".":
                        for c in '123456789':
                            #function call which determines th three conditions
                            # 1. row wise uniqueness
                            # 2. column wise uniqueness
                            # 3. 3*3 sub boxes uniqueness
                            if isValid(board, i, j, c):
                                board[i][j] = c

                                if solve(board):
                                    return True
                                else:
                                    #backtracing
                                    board[i][j] = "."
                        return False
            return True
        
        def isValid(board, row, col, c):
            for i in range(9):
                if board[i][col] == c:
                    return False
                if board[row][i] == c:
                    return False
                if (board[3*(row//3)+i//3][3*(col//3)+i%3] == c):
                    return False

            return True
        solve(board)