'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

Example:

Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
* All elements in the array are in the range [0, N-1]
* N * N does not overflow for a signed integer
'''

A = [4, 0, 2, 3, 1]

def rearrangeArray(A):

    n = len(A)

    for i, val in enumerate(A):
        A[i] = A[i] + (A[A[i]] % n) * n

    for i, val in enumerate(A):
        A[i] = A[i] / n

    return A

print rearrangeArray(A)