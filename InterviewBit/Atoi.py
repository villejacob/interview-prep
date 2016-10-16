'''
Implement atoi to convert a string to an integer.

Example :

Input : "9 2704"
Output : 9
Note: There might be multiple corner cases here. Clarify all your doubts using "See Expected Output".
Questions: Q1. Does string contain whitespace characters before the number?
A. Yes Q2. Can the string have garbage characters after the number?
A. Yes. Ignore it. Q3. If no numeric character is found before encountering garbage characters, what should I do?
A. Return 0. Q4. What if the integer overflows?
A. Return INT_MAX if the number is positive, INT_MIN otherwise.
Warning : DO NOT USE LIBRARY FUNCTION FOR ATOI.
If you do, we will disqualify your submission retroactively and give you penalty points.
'''

A = "    160254 f327    "

def atoi(A):

    def is_int(c):
        try:
            int(c)
            return True
        except ValueError:
            return False

    charArray = list(A)
    INT_MAX = 2147483647
    sign = 1
    i = 0
    num = str(0)

    while A[i] == ' ':
        i += 1

    if A[i] == '+':
        i += 1
    elif A[i] == '-':
        sign = -1
        i += 1

    while i < len(A):
        if not is_int(A[i]):
            break
        num += (A[i])
        if abs(int(num)) > INT_MAX/10 and i != len(A) - 1:
            if is_int(A[i+1]):
                if sign < 0:
                    return INT_MAX*sign - 1
                else: return INT_MAX
        elif abs(int(num)) == INT_MAX/10 and i != len(A) - 1:
            if is_int(A[i+1]) and int(A[i+1]) > 7:
                if sign < 0:
                    return INT_MAX*sign - 1
                else: return INT_MAX
        i += 1

    return int(num)*sign

print atoi(A)