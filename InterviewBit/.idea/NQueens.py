'''
The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
 queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Example: A = 5

Expected output is:

[   . . . . Q       [   . . . . Q       [   . . . Q .       [   . . . Q .       [   . . Q . .
    . . Q . .           . Q . . .           . Q . . .           Q . . . .           . . . . Q
    Q . . . .           . . . Q .           . . . . Q           . . Q . .           . Q . . .
    . . . Q .           Q . . . .           . . Q . .           . . . . Q           . . . Q .
    . Q . . .   ]       . . Q . .   ]       Q . . . .   ]       . Q . . .   ]       Q . . . .   ]

[   . . Q . .       [   . Q . . .       [   . Q . . .       [   Q . . . .       [   Q . . . .
    Q . . . .           . . . . Q           . . . Q .           . . . Q .           . . Q . .
    . . . Q .           . . Q . .           Q . . . .           . Q . . .           . . . . Q
    . Q . . .           Q . . . .           . . Q . .           . . . . Q           . Q . . .
    . . . . Q   ]       . . . Q .   ]       . . . . Q   ]       . . Q . .   ]       . . . Q .   ]

'''


class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):

        # Create full row of the board as an index, ans as solution set
        stack, ans = [[(0, i)] for i in range(A)], []

        # While the stack is not empty
        while stack:

            # Records
            board = stack.pop()

            # Increments for each pop from the stack
            row = len(board)

            # For the final row print the output in terms of '.'s and 'Q's
            if row == A:
                ans.append([''.join('Q' if i == c else '.' for i in range(A))
                            for r, c in board])

            # Iterate through each column per row
            for col in range(A):

                # Check if column, row, or diagonals are already occupied
                if all(col != c and abs(row-r) != abs(col-c) for r, c in board):

                    # Place a queen at this row and column, record this pair per this board
                    stack.append(board + [(row, col)])

        return ans

mySolution = Solution()
print mySolution.solveNQueens(5)


