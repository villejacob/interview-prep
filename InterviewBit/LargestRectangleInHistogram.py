'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
the largest rectangle in the histogram.

Example Histogram

             _6_
         _5_|   |
        |   |   |
        |   |   |    _3_
 _2_    |   |   |_2_|   |
|   |_1_|   |   |   |   |
|___|___|___|___|___|___|

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

             _6_
         _5_|   |
        |/ / / /|
        | / / / |    _3_
 _2_    |/ / / /|_2_|   |
|   |_1_| / / / |   |   |
|___|___|/_/_/_/|___|___|

The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):

        # Initial thoughts:
        # O(n^2) solution is to iterate through list starting at each index, and finding the area
        # as the min height x current width

        # area = 0
        #
        # for i, height in enumerate(A):
        #     for j, current_height in enumerate(A[i:], i):
        #         height = min(height, current_height)
        #         area = max(area, (j-i+1)*height)
        #
        # return area

        # More optimal DP solution with memoization:
        # Calculate current area up, then sum right.
        # Ex: [2, 1, 5, 6, 2, 3]
        #
        #           6                       6
        #        5  5                    5 10
        #        4  4                    4  8
        #        3  3     3   ->         3  6     3
        #  2     2  2  2  2        2     2  4  6  8
        #  1  1  1  1  1  1        1  2  3  4  5  6
        #
        # The max area is the max value from this array

        # if not A:
        #     return 0
        #
        # if len(A) == 1:
        #     return A[0]
        #
        # # Find max histogram height
        # max_height = A[0]
        # for val in A:
        #     max_height = max(max_height, val)
        #
        # # Create double array as shown above, filling in 0 for missing values
        # area = [[0 for x in xrange(max_height)] for y in xrange(len(A))]
        # for row in xrange(len(A)):
        #     for height in xrange(A[row]):
        #         area[row][height] = height+1
        #
        # for row in area:
        #     print row
        #
        # max_area = area[0][-1]
        #
        # # Add the height of the last row to the current to find area at that width and height
        # for row in xrange(1, len(A)):
        #     for height in xrange(A[row]):
        #         area[row][height] = area[row-1][height] + height+1
        #         max_area = max(max_area, area[row][height])
        #
        # for row in area:
        #     print row
        #
        # return max_area

        # Still not optimal because complexity is O(n x (max-val in A))

        # Attempt 3: Use stacks
        # If the height of the next bar is larger, add to the stack. Otherwise find the height of all the bars less
        # than the current bars height, while popping from the stack so it is not calculated again
        #
        # Visual representation:
        #
        #   1 < 2: Calculate area of bars larger than 1 (max area of eliminated = 2)
        #
        #              _6_                                _6_
        #          _5_|   |                           _5_|   |
        #         |   |   |                          |   |   |
        #         |   |   |    _3_                   |   |   |    _3_
        #  _2_    |   |   |_2_|   |      ->          |   |   |_2_|   |
        # | x |_1_|   |   |   |   |               _1_|   |   |   |   |
        # |_x_|___|___|___|___|___|              |___|___|___|___|___|
        #
        #   2 < 6: Caluclate area of bars larger than 2 (max area of eliminated = 10)
        #
        #          _6_
        #      _5_|   |
        #     | x | x |
        #     | x | x |    _3_                        _3_
        #     | x | x |_2_|   |      ->           _2_|   |
        #  _1_| x | x |   |   |               _1_|   |   |
        # |___|_x_|_x_|___|___|              |___|___|___|
        #
        # Then after all values have been added to the stack at one point, calculate the area of descending height

        stack = []
        i = 0
        area = A[0]

        # Add increasing values to the stack
        while i < len(A):
            if len(stack) == 0 or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                last_area = A[stack.pop()]*(i if len(stack) == 0 else i - stack[-1] - 1)
                area = max(area, last_area)

        while len(stack) != 0:
            last_area = A[stack.pop()] * (i if len(stack) == 0 else i - stack[-1] - 1)
            area = max(area, last_area)

        return area



A1 = [2, 1, 5, 6, 2, 3]
A2 = [98]
soln = Solution()
print soln.largestRectangleArea(A1)
