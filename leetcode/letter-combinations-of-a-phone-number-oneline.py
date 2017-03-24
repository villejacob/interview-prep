'''
Interesting one-line solution to this problem using reduce
'''

class Solution(object):
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):

        if digits == '': return []

        kvmaps = {
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'
                }

        return reduce(lambda acc, digit: [x + y for x in acc for y in
            kvmaps[digit]], digits, ['']) 

print Solution().letterCombinations("234")
