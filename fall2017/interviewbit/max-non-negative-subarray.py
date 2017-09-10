'''
Find out the maximum sub-array of non negative numbers from an array.
The sub-array should be continuous. That is, a sub-array created by choosing
the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the
sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]

NOTE:   If there is a tie, then compare with segment's length and return
        segment which has maximum length
NOTE 2: If there is still a tie, then return the segment with minimum
        starting index
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        capture_subarray = False
        start = current_sum = current_length = 0
        max_start = max_sum = max_length = 0

        for i, value in enumerate(A):
            if value >= 0:
                if capture_subarray == False:
                    capture_subarray = True
                    start = i
                current_sum += value
                current_length += 1
                if current_sum > max_sum:
                    max_start = start
                    max_sum = current_sum
                    max_length = current_length
                elif current_sum == max_sum:
                    if current_length > max_length:
                        max_start = start
                        max_sum = current_sum
                        max_length = current_length
                    elif current_length == max_length:
                        if A[start] < A[max_start]:
                            max_start = start
                            max_sum = current_sum
                            max_length = current_length
            else:
                capture_subarray = False
                current_sum = 0
                current_length = 0
                    
                

        return A[max_start : max_start + max_length]

A = [1, 2, 5, -1, -2, 4, 1, 3]
B = [4, 1, 3, -1, -2, 1, 2, 5]
C = [0, 0, -1, 0]
solution = Solution()
print solution.maxset(C)
