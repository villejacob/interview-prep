'''
Find the kth smallest element in an unsorted array of non-negative integers.

Definition of kth smallest element

 kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then A[k - 1] ( k is 1 based, while the arrays are 0 based )
NOTE
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.

Example:

A : [2 1 4 3 2]
k : 3

answer : 2
'''

import heapq

A = [2, 1, 4, 3, 2]
k = 3

def kthSmallest(A, k):

    heap = []

    for i, val in enumerate(A):
        if i < k:
            heapq.heappush(heap, -val)
        elif val < abs(heap[0]):
            heapq.heapreplace(heap, -val)

    return -heap[0]

print kthSmallest(A, k)