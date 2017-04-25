'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
containing only 1's and return its area.

For example, given the following matrix:

    1 0 1 0 0       - - - - -
    1 0 1 1 1   =>  - - 1 1 1   =>  return 6       
    1 1 1 1 1       - - 1 1 1
    1 0 0 1 0       - - - - -
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height = [0 for n in xrange(len(matrix[0]) + 1)]
        ans = 0

        for row in matrix:
            for i in xrange(len(matrix[0])):
                if row[i] == '1':
                    height[i] = height[i] + 1
                else:
                    height[i] = 0
                stack = [-1]
                for i in xrange(len(matrix[0]) + 1):
                    while height[i] < height[stack[-1]]:
                        h = height[stack.pop()]
                        w = i - 1 - stack[-1]
                        ans = max(ans, w * h)
                    stack.append(i)
        return ans

matrix = [  ['1', '0', '1', '0', '0'],
            ['1', '0', '1', '1', '1'],
            ['1', '1', '1', '1', '1'],
            ['1', '0', '0', '1', '0']]

print Solution().maximalRectangle(matrix)
