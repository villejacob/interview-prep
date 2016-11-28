'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note1: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer.
For example,
given strings "12", "10", your answer should be "120".

NOTE : DO NOT USE BIG INTEGER LIBRARIES ( WHICH ARE AVAILABLE IN JAVA / PYTHON ).
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):

        # Edge case where a string is empty
        if len(A) == 0 or len(B) == 0:
            return ""

        a = ""
        b = ""
        res = ""
        ans = []

        # Collect all consecutive digits from the back of A and B
        for char in A[::-1]:
            if char.isdigit():
                a += char
            else:
                break

        for char in B[::-1]:
            if char.isdigit():
                b += char
            else:
                break

        # ensure that b is the larger value
        if len(a) > len(b):
            a, b = b, a

        # If multiplying a and b will create overflow, return subtraction of appended size and a
        # if int(b) > (2147483647 / int(a)):
        #     for zero in xrange(10 - len(b)):
        #         b += '0'
        #     return str(int(b) - int(a))

        # Multiplication: calculated in reverse
        # Append 0 for decimal place
        # Multiply each value in a with each value in b
        for zeros, a_char in enumerate(a):
            res += '0' * zeros
            for b_char in b:
                res += str(int(a_char)*int(b_char))
            ans.append(res)
            res = ""

        # Reverse items in ans
        ans = [string[::-1] for string in ans]
        for string in ans:
            res = (int(string) + int(res))

        return res


A1 = "12"
B1 = "10"
soln = Solution()
print soln.multiply(A1, B1)