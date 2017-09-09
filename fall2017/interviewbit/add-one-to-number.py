'''
Given a non-negative number represented as an array of digits,
add 1 to the number (increment the number represented by the digits).

The most significant digit is at the head of the list.

Example:

    If the vector has [1, 2, 3] the returned vector should be [1, 2, 4]
    as 123 + 1 = 124.

 NOTE: Certain things are intentionally left unclear in this question which you
 should practice asking the interviewer.

 For example, for this problem, following are some good questions to ask :

     Q : Can the input have 0's before the most significant digit. Or in other
         words, is 0 1 2 3 a valid input?
     A : For the purpose of this question, YES

     Q : Can the output have 0's before the most significant digit? Or in other
         words, is 0 1 2 4 a valid output?
     A : For the purpose of this question, NO. Even if the input has zeroes before
     the most significant digit.
 '''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A.reverse()
        carry = 1
        for i, val in enumerate(A):
            res = (val + carry)%10
            if res != 0:
                carry = 0
            A[i] = res

        if carry:
            A.append(1)

        A.reverse()

        start = 0
        for i, val in enumerate(A):
            if val != 0:
                start = i
                break

        return A[start:]

A = [1, 2, 3, 9] 
soln = Solution()
print soln.plusOne(A)