'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

    1: 1        2: abc      3: def
    4: ghi      5: jkl      6: mno
    7: pqrs     8: tuv      9: wxyz
                0: 0

The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.
'''

class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):

        if not A:
            return []

        dict = {"0": ["0"], "1": ["1"], "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

        # Depth first search of a string, current index, path, and result
        def dfs(dict, string, index, path, res):

            # If the index is outside the string, start to append result
            if index == len(string):
                res.append(path)
                return

            # Iterate through length of dictionary entry
            for i in dict[string[index]]:

                # Call method again with incremented index (keep track of level) and the path (dict entry value)
                dfs(dict, string, index + 1, path + i, res)

        res = []
        dfs(dict, A, 0, "", res)
        return res

mySolution = Solution()
print mySolution.letterCombinations("23")
