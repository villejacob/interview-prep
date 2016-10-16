'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120
Number of trailing zeros = 1
So, return 1
'''

A = 9247

def trailingZeros(A):

    A = abs(A)

    ans = 0
    i = 1
    while A / 5 ** i >= 1:
        ans += A / 5 ** i
        A /= 5 ** i

    return ans

print trailingZeros(A)