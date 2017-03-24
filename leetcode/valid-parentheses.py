'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s: return False

        pairs = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for item in s:
            if item in pairs.values():
                stack.append(item)
            elif item in pairs.keys():
                if len(stack) == 0 or pairs[item] != stack.pop():
                    return False
                 
        return len(stack) == 0

soln = Solution()
print soln.isValid("[((()))]")
