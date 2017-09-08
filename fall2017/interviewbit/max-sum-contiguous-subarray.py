'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4], the contiguous
subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        if not A: return A

        ans = A[0]
        sum = 0
        
        for val in A:
            sum += val
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0

        return ans

A = [-2,1,-3,4,-1,2,1,-5,4]
soln = Solution()
print soln.maxSubArray(A)
