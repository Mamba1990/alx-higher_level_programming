#!/usr/bin/python3
"""Solving the N-queens puzzle.

Attributes:
    board (list): list of lists that represents the chessboard.
    _solutions (list): list of lists that contains solutions.
"""
import sys


def initBoard(m):
    """Initializingan `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for k in range(m)]
    [row.append(' ') for k in range(m) for row in board]
    return (board)


def boardDeepcopy(board):
    """Displays a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(boardDeepcopy, board))
    return (board)


def getSolution(board):
    """Dsiplays the list of lists representation of a solved chessboard."""
    _solution = []
    for rr in range(len(board)):
        for cc in range(len(board)):
            if board[rr][cc] == "Q":
                _solution.append([rr, cc])
                break
    return (_solution)


def x_out(board, row, colm):
    """spots on a chessboard.


    Args:
        board (list): actual working chessboard.
        row (int): row where a queen played last.
        colm (int): The column where a queen was last played.
    """
    # all forward spots
    for cc in range(colm + 1, len(board)):
        board[row][cc] = "x"
    # all backwards spots
    for cc in range(colm - 1, -1, -1):
        board[row][cc] = "x"
    # all spots below
    for rr in range(row + 1, len(board)):
        board[rr][colm] = "x"
    # all spots above
    for rr in range(row - 1, -1, -1):
        board[rr][colm] = "x"
    # all spots diagonally down to the right
    cc = colm + 1
    for rr in range(row + 1, len(board)):
        if cc >= len(board):
            break
        board[rr][cc] = "x"
        cc += 1
    # all spots diagonally up to the left
    cc = colm - 1
    for rr in range(row - 1, -1, -1):
        if cc < 0:
            break
        board[rr][cc]
        cc -= 1
    # all spots diagonally up to the right
    cc = colm + 1
    for rr in range(row - 1, -1, -1):
        if cc >= len(board):
            break
        board[rr][cc] = "x"
        cc += 1
    # all spots diagonally down to the left
    cc = colm - 1
    for rr in range(row + 1, len(board)):
        if cc < 0:
            break
        board[rr][cc] = "x"
        cc -= 1


def recursiveSolve(board, row, queen, _solutions):
    """solve recuisively an N-queens puzzle.

    Args:
        board (list): actual working chessboard.
        row (int): actual working row.
        queen (int): actual number of placed queens.
        _solutions (list): list of lists of solutions.
    Returns:
        solutions
    """
    if queen == len(board):
        _solutions.append(getSolution(board))
        return (_solutions)

    for cc in range(len(board)):
        if board[row][cc] == " ":
            tmp_board = boardDeepcopy(board)
            tmp_board[row][cc] = "Q"
            x_out(tmp_board, row, cc)
            _solutions = recursiveSolve(tmp_board, row + 1,
                                        queen + 1, _solutions)

    return (_solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initBoard(int(sys.argv[1]))
    _solutions = recursiveSolve(board, 0, 0, [])
    for solu in _solutions:
        print(solu)
