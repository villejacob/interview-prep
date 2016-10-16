'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based.
Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.

Input: [2, 7, 11, 15], target=9
Output: index1 = 1, index2 = 2
'''

A = [2, 7, 11, 15]
B = 9

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def twoSum(self, A, B):

        hashmap = {}

        for index, val in enumerate(A):

            # When the value is already in the hashmap
            # Implies that the key + another already reached value sums to the target
            if val in hashmap:

                # Return the index of the first and second numbers that sum to the target
                return [hashmap[val] + 1, index + 1]

            # Key = value needed to reach the target, store the index of this value for this key
            if (B - val) not in hashmap:
                hashmap[B - val] = index

        # When no pair is found return empty list
        return []

mySolution = Solution()
print mySolution.twoSum(A, B)