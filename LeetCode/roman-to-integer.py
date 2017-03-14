'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

        if len(s) == 1:
        	return roman[s]

        res = 0
        prev = 1001

        for i, letter in enumerate(s):
        	res += roman[letter]
        	if roman[letter] > prev:
        		res -= (2 * prev)
        	prev = roman[letter]

        return res


soln = Solution()
print soln.romanToInt("XCIV")