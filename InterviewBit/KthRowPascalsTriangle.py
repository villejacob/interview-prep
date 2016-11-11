'''
Given an index k, return the kth row of the Pascal's triangle.

Pascal's triangle : To generate A[C] in row R, sum up A'[C] and A'[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
 NOTE : k is 0 based. k = 0, corresponds to the row [1].
Note:Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        # Initialize pascals triangle as double array with first & second row with 1 (memoization)
        pascal = [[1], [1, 1]]
        # For each row greater than 1 up to and including A
        for i in xrange(2, A+1):
            row = [1]
            # Generate values up to but not including the final value
            for j in xrange(1, i):
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            # Add 1 as the last value
            row.append(1)
            pascal.append(row)

        return pascal

# Integer input
n = 5

soln = Solution()
triangle = soln.getRow(n)

# Answer is triangle[n]
print triangle[n]

# Prints the whole triangle
# for row in triangle:
#     print row
