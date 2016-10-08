'''

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example:

Given the array [-2,1,-3,4,-1,2,1,-5,4],

the contiguous subarray [4,-1,2,1] has the largest sum = 6.

For this problem, return the maximum sum.

'''


# Solves using divide and conquer O(nlogn)

# def max_subarray_sum(A):
#     def mss(A, size):
#
#         if size == 1:
#             return A[0]
#
#         mid = size / 2
#
#         left_mss = mss(A[:mid], len(A[:mid]))
#         right_mss = mss(A[mid:], len(A[mid:]))
#
#         left_sum, right_sum = (-2147483648,) * 2
#         current_sum = 0
#
#         for val in reversed(A[:mid]):
#             current_sum += val
#             left_sum = max(left_sum, current_sum)
#
#         current_sum = 0
#
#         for val in A[mid:]:
#             current_sum += val
#             right_sum = max(right_sum, current_sum)
#
#         both_sum = left_sum + right_sum
#         return max(both_sum, left_mss, right_mss)
#
#     return mss(A, len(A))


# Solution in O(n)

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def max_subarray_sum(A):

	# Set ans to the first element, handles situation when all are negative
    ans = A[0]

    # Because the value will be added to this, it is 0, not MAX_INT or MIN_INT
    sum = 0

    for val in A:

    	# Add the value to the current sum
        sum += val

        # If the sum is greater than the max, record the sum as ans
        if sum > ans: ans = sum

        # If the sum ever drops below 0, reset the sum to 0. Allows the 
        if sum < 0: sum = 0

    return ans


print max_subarray_sum(A)
