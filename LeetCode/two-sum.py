'''
Given an array of integers, return indices of the two 
numbers such that they add up to a specific target.

You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Notes:
# Store the difference rather than the value. Automatically
# grabs the first instance this way, and only requires
# one pass through the array.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) <= 1:
        	return None

        diff_dict = dict()

        for i, val in enumerate(nums):
        	if val in diff_dict:
        		return [diff_dict[val], i]
        	else:
        		diff_dict[target - val] = i

        return None

test_list = [2, 6, 4, 8]
test_target = 6

soln = Solution()
print soln.twoSum(test_list, test_target)