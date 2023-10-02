#!/usr/bin/python3
"""
Solves the N-queens puzzle.
Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.
"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    return [[' ' for _ in range(n)] for _ in range(n)]

def is_safe(board, row, col):
    """Check if it's safe to place a queen at the given row and column."""
    n = len(board)

    if 'Q' in board[row]:
        return False

    if 'Q' in [board[i][col] for i in range(n)]:
        return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    def backtrack(row):
        if row == n:
            solutions.append([''.join(row) for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = ' '

    board = init_board(n)
    solutions = []
    backtrack(0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for sol in solutions:
        for row in sol:
            print(row)
        print()
