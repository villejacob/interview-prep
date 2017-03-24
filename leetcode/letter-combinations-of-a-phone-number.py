'''
Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below.

1:      2:abc   3:def
4:ghi   5:jkl   6:mno
7:pqrs  8:tuv   9:wxyz
        0:

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
    Although the above answer is in lexicographical order, your answer could be
    in any order you want.
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits: return []

        phone = {'0' : [''], '1' : [''], '2' : ['a', 'b', 'c'], 
                '3' : ['d', 'e', 'f'], '4' : ['g', 'h', 'i'], 
                '5' : ['j', 'k', 'l'], '6' : ['m', 'n', 'o'], 
                '7' : ['p', 'q', 'r', 's'], '8' : ['t', 'u', 'v'],
                '9' : ['w', 'x', 'y', 'z']}

        final = []

        def getLetters(digit_str, current_str):
            if len(digit_str) == 0:
                final.append(current_str)
                return
            for letter in phone[digit_str[0]]:
                getLetters(digit_str[1:], current_str + letter)


        getLetters(digits, "")

        return final

soln = Solution()
number_string = "23"
print soln.letterCombinations(number_string)
