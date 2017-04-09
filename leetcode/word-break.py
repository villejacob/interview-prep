'''
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence
of one or more dictionary words. You may assume the dictionary does not contain
duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''
class Solution(object):
    # Intuitive solution in O(n^2)
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        return self.breakHelper(s, wordSet)
    
    def breakHelper(self, s, wordDict):
        if s in wordDict:
            return True
        for i in xrange(len(s)):
            if s[:i] in wordDict:
                if self.breakHelper(s[i:], wordDict):
                    return True
        return False

    def wordBreakDP(self, s, wordDict):
        memo = [False] * len(s)  
        for i in xrange(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] \
                        and (memo[i-len(w)] or i-len(w) == -1):
                            memo[i] = True
        return memo[-1]


wordDict1 = ["leet", "code"]
wordDict2 = ["so", "soda", "dap", "pop"]
print Solution().wordBreakDP("leetcode", wordDict1)                
print Solution().wordBreakDP("sodapop", wordDict2)
