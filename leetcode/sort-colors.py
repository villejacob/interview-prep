'''
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white
and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.
'''

def sortColors(n):
    """
    :type n: List[int]
    :rtype: void Do not return anything, modify nums in-place
    instead.
    """
    low = 0
    high = len(n)-1
    i = 0

    while i < len(n) and low < high:
        if n[i] == 2 and i < high:
            n[i], n[high] = n[high], n[i]
            high -= 1
        elif n[i] == 0 and i > low:
            n[i], n[low] = n[low], n[i]
            low += 1
        else:
            i += 1

nums = [1, 1, 0, 2, 1, 0, 1, 2]
print nums
sortColors(nums)
print nums
