'''
A robot is located at the top-left corner of an A x B grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

[ START ]   [  ]    [  ]    [  ]
[  ]        [  ]    [  ]    [  ]
[  ]        [  ]    [  ]    [  ]
[  ]        [  ]    [  ]    [ FINISH ]


How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.

Example :

Input : A = 2, B = 2
Output : 2

2 possible routes : (0, 0) -> (0, 1) -> (1, 1)
              OR  : (0, 0) -> (1, 0) -> (1, 1)
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):

        # Thought process:
        # The intuitive way to do this would be to do a DFS and count each path that finds finish
        # Because it only needs to return the number, not the path, curious if possible to find
        #   the number of paths without going through all of them
        # Deciding to go ahead and do DFS recursively (mostly for practice)

        # # Edge cases when A or B is 1
        # if A == 1 or B == 1:
        #     return 1
        #
        # def DFS(x, y, A, B):
        #     # Base case when out of bounds, add nothing
        #     if x >= A or y >= B:
        #         return 0
        #     # If the path is found, add to count
        #     if x == A - 1 and y == B - 1:
        #         return 1
        #     # Otherwise, go right and go down
        #     return DFS(x + 1, y, A, B) + DFS(x, y + 1, A, B)
        #
        # return DFS(0, 0, A, B)

        # While working on that I thought of a mathematical approach:
        #   The spaces above and to the left of Finish each have only one path that goes to the finish
        #   Above the space above has only one path, also all to the left of left have only one path
        #   However: outside the range, the number of paths is the sum of num paths below and right!

        # Mathematical approach with memoizaiton:

        # Create array of paths for each location
        path_count = [[1] * A for val in xrange(B)]
        # Iterate from value top left of the destination to the start
        for row in xrange(B - 2, -1, -1):
            for col in xrange(A - 2, -1, -1):
                path_count[row][col] = path_count[row + 1][col] + path_count[row][col + 1]
        # # Print path_count matrix
        # for row in path_count:
        #     print row
        # Number of paths at the start is the total number of paths
        return path_count[0][0]


A = 4
B = 4
soln = Solution()
print soln.uniquePaths(A, B)
