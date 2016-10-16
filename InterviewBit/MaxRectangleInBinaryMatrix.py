'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Bonus if you can solve it in O(n^2) or less.

Example :

A : [  1 1 1
       0 1 1
       1 0 0
    ]

Output : 4

As the max area rectangle is created by the 2x2 rectangle created by (0,1), (0,2), (1,1) and (1,2)
'''

A = [[1, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
# A = [[1]]
# A = [[1, 1], [1, 1]]

for row in xrange(len(A)):
    print A[row]

print ""

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):

        row_max = [[0 for column in range(len(A[0]))] for row in range(len(A))]

        num_rows = len(A)
        num_cols = len(A[0])

        if num_rows == 0: return 0
        if num_cols == 0: return 0

        max_area = 0

        for row in xrange(num_rows):
            for col in xrange(num_cols):
                if A[row][col] == 1:

                    # Count the max across the row
                    if col == 0:
                        row_max[row][col] = 1
                    else:
                        row_max[row][col] = row_max[row][col - 1] + 1

                    y = 1
                    x = num_cols

                    # Find new max area by iterating upwards, finding the new row max and is a 1
                    while (row - y + 1 >= 0) and (A[row - y + 1][col] == 1):
                        # Set x (current row max) to this row's max when smaller
                        x = min(row_max[row - y + 1][col], x)
                        max_area = max(max_area, x * y)
                        y += 1

        return max_area, row_max



sol = Solution()
soln, row_max = sol.maximalRectangle(A)
print "Answer: ", soln

