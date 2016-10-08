'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0

NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
'''

A = [4, 5, 6, 7, 0, 1, 2]
B = 5

def search(A, B):

    start = 0
    end = len(A) - 1

    while start <= end:

        mid = start + (end - start)/2

        if B == A[mid]: return mid
        elif B == A[end]: return end
        elif B == A[start]: return start

        if A[mid] > A[end]:                     # Assume left is sorted
            if B < A[mid] and B > A[end]:
                start += 1
                end = mid - 1
            elif B < A[end] or B > A[mid]:
                start = mid + 1
                end -= 1
        elif A[mid] < A[start]:                 #Assume right is sorted
            if B > A[mid] and B < A[start]:
                start = mid + 1
                end -= 1
            elif B < A[mid] or B > A[start]:
                start += 1
                end = mid - 1
        elif A[start] <= A[end]:                #Assume all storted
            if B > A[mid]:
                start = mid + 1
                end -= 1
            else:
                start += 1
                end = mid - 1
        else: return -1
    return -1

print search(A, B)