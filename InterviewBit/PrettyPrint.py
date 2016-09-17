'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
Example 2:

Input: A = 3.
Output:

3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.

You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
'''

A = 6

def prettyPrint(A):

    if A == 0:
        return

    final = (2*A) - 1

    row_col = 0
    max_row_col = final - 1

    ans = [[0] * final for i in range(final)]

    while row_col <= max_row_col:
        for i in range(row_col, max_row_col + 1):
            ans[row_col][i] = A
            ans[max_row_col][i] = A
            ans[i][row_col] = A
            ans[i][max_row_col] = A
        row_col += 1
        max_row_col -= 1
        A -= 1

    return ans

ans = prettyPrint(A)

for i in range(2*A-1):
    print ans[i], "\n"