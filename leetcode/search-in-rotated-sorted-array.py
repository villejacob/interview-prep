'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        lo = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo)/2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                if nums[lo] <= nums[mid] and target < nums[lo]:
                    lo = mid+1
                else:                  
                    hi = mid-1
            else:
                if nums[hi] >= nums[mid] and target > nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1
        return -1


print Solution().search([4, 5, 6, 7, 0, 1, 2], 8)
