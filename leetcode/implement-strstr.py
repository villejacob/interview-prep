'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle: return 0
        n = len(needle)
        for i in xrange(len(haystack)):
            if haystack[i:i+n] == needle:
                return i
        return -1

print Solution().strStr("aaabc", "a")

