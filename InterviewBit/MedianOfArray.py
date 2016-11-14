'''
There are two sorted arrays A and B of size m and n respectively.

Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).

The overall run time complexity should be O(log (m+n)).

Sample Input

A : [1 4 5]
B : [2 3]

Sample Output: 3

 NOTE: IF the number of elements in the merged array is even,
 then the median is the average of n / 2 th and n/2 + 1th element.

For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):

        # Ensure that B is the larger array
        if len(A) > len(B):
            A, B = B, A

        a_len = len(A)
        b_len = len(B)

        # If array length is 0, return median of other
        if a_len == 0:
            # If even, return avg of center 2 elements
            if not b_len % 2:
                return (B[b_len/2-1] + B[(b_len/2)])/2.0
            # If odd, return center element
            return B[b_len/2]

        if b_len == 0:
            if not a_len % 2:
                return (A[a_len/2-1] + A[(a_len/2)])/2.0
            return A[a_len/2]

        low = 0
        high = a_len

        while low <= high:
            # Keep track of two medians, the sum of both is equal to the median index
            # Median of A
            i = (low + high) / 2
            # Median of B (related to A to maintain i + j = index)
            j = (a_len + b_len + 1)/2 - i

            # If either: i is at the beginning of A, j is at the end of B, or A's median value is less than B's
            # AND either: j is at the beginning of B, i is at the end of A, or B's median value is less than A's
            # TLDR: The median is found
            if (j == 0 or i == a_len or B[j-1] <= A[i]) and (i == 0 or j == b_len or A[i-1] <= B[j]):
                # If the sum is odd: return the center element
                if (a_len + b_len) % 2:
                    # if i is at the beginning of A
                    if i == 0:
                        # The median of both is the median value at B
                        return B[j-1]
                    if j == 0:
                        # The median of both is the median value at A
                        return A[i-1]
                    # If the median is within both A and B, find the max value
                    return max(A[i-1], B[j-1])
                # If the sum is even: return the average of the center 2 elements
                else:
                    # If i is at the beginning of A, return med val of B and the next largest element
                    if i == 0:
                        return (B[j-1] + min(A[i], B[j]))/2.0
                    # If j is at the beginning of B, return med val of A and the next largest element
                    if j == 0:
                        return (A[i-1] + min(A[i], B[j]))/2.0
                    # If i is at the end of A, return the med val of B and the next smallest element
                    if i == a_len:
                        return (B[j] + max(A[i-1], B[j-1]))/2.0
                    # If j is at the end of B, return the med val of A and the next smallest element
                    if j == b_len:
                        return (A[i] + max(A[i-1], B[j-1]))/2.0
                    # If med of both is located within A and B, average the smallest and largest in each
                    return (max(A[i-1], B[j-1]) + min(A[i], B[j]))/2.0
            # Otherwise, if at bounds or mid B is larger than A, continue binary search in upper division
            elif j == 0 or i == a_len or B[j-1] > A[i]:
                low = i + 1
            # If at bounds or mid A is larger than B, continue binary search in lower division
            elif i == 0 or j == b_len or A[i-1] > B[j]:
                high = i - 1
        return -1


A1 = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9, 10, 11, 12]
B1 = [1, 5, 6, 7, 8, 9]
soln = Solution()
print soln.findMedianSortedArrays(A1, B1)

