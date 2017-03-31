'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
    
Some examples:
    isMatch("aa","a") -> false
    isMatch("aa","aa") -> true
    isMatch("aaa","aa") -> false
    isMatch("aa", "a*") -> true
    isMatch("aa", ".*") -> true
    isMatch("ab", ".*") -> true
    isMatch("aab", "c*a*b") -> true
'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        #if not s or not p:
        #    return s == p

        i = 0
        for j in xrange(len(p)):
            if j < len(p)-1 and p[j+1] != '*':
                j += 1
            elif self.isMatch(s, p[j+2:]):
                return True
            if i == len(s) or (p[j] != s[i] and p[j] != '.'):
                return False
            i += 1
        return i == len(s)


print Solution().isMatch("aab", "c*a*b")
