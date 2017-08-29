class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        b %= len(a)
        for i in xrange(b, len(a)):
            ret.append(a[i])
        for j in xrange(b):
            ret.append(a[j])
        return ret

soln = Solution()
print soln.rotateArray([1, 2, 3, 4, 5, 6], 8)
