'''
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Example:
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
'''

A = [-6, -7, -7, 2, 3, 3, 3, 3, 4, 4, 5, 6, 7, 7, 7]

def removeDuplicates(A):

    i = 0
    j = i + 1

    while j < len(A):
        if A[i] == A[j]:
            j += 1
        else:
            i += 1
            A[i] = A[j]
            j += 1

    return len(A[:i+1])

print removeDuplicates(A), A