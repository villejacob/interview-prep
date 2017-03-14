'''
Given an array S of n integers, are there elements a, b, c in S 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Approach: Use O(n) solution for 2Sum for each value
        #	using a + b = -c, where -c is the target

        # if len(nums) < 3:
        # 	return []

        # # Sort w/ Timsort in O(n log n)
        # nums.sort()
        # ret = set()
        # num_hash = {}

        # for i, target in enumerate(nums):
        # 	for j, val in enumerate(nums[i+1:], 1):
        # 		third = -target - val
        # 		if third in num_hash and num_hash[third] != i + j and num_hash[third] != i:
        # 			three = [target, val, third]
        # 			three.sort()
        # 			ret.add(tuple(three))
        # 		else:
        # 			num_hash[val] = i + j

        # # Convert set of tuples into list of lists
        # return [list(tup) for tup in ret]

        # Approach 2: Use two pointers
        
        nums.sort()

        if len(nums) < 3:
        	return []
        elif nums[0] == nums[-1] and nums[0] == 0:
        	return [[0, 0, 0]]    	

        ret = set()

        for i, base in enumerate(nums[:-2]):
        	low = i+1
        	high = len(nums)-1
        	while high > low:
        		three_sum = base + nums[low] + nums[high]
        		if three_sum == 0:
        			ret.add((base, nums[low], nums[high]))
        			low += 1
        			high -= 1
        		elif three_sum > 0:
        			high -= 1
        		elif three_sum < 0:
        			low += 1

        return [list(tup) for tup in ret]


soln = Solution()
test_nums = [-1, 0, 1, 4, 2, -1]
# test_nums = [1, -1, 2, -2]
# test_nums = [0, 0, 0]
print soln.threeSum(test_nums)
