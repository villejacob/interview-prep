'''
Implement int sqrt(int x).

Compute and return the square root of x.

If x is not a perfect square, return floor(sqrt(x))

Example :

    Input : 11
    Output : 3
'''
import math

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        low, high, ans = 1, A, 0

        # Binary search for root
        while low <= high:
            current = (high - low)/2 + low
            if current**2 <= A: 
                low = current + 1
                ans = current
            else:
                high = current - 1
        return ans

print Solution().sqrt(9)
print Solution().sqrt(10)
print Solution().sqrt(11)
print Solution().sqrt(12)
print Solution().sqrt(13)
print Solution().sqrt(16)
