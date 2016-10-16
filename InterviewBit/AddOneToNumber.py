'''
Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

Note: Input may have trailing 0's, output cannot
'''

A = [0, 0, 9, 9, 9, 9, 9]

def plusOne(A):

    msb = 0
    while A[msb] == 0 and len(A) > 1:                   # Find index of most significant bit
        msb += 1

    i = len(A) - 1
    ans = [0]*(len(A) - msb)

    # Scenario 1: Only changes lsb
    if A[i] != 9:                                       # If lsb is not 9 add one
        ans[i - msb] = A[i] + 1
        i -= 1
        while i >= msb:                                 # Copy rest
            ans[i - msb] = A[i]
            i -= 1

    # Scenario 2: Series of 9's
    else:
        while A[i] == 9:                                # For a sequence of at least on 9
            ans[i - msb] = 0                            # Set to 0
            if i == msb:                                # If this was the msb add one to beginning of list
                ans = [1] + ans
                return ans
            i -= 1                                      # Check left for next digit
            if A[i] != 9:                               # If non-9 is reached
                ans[i - msb] = A[i] + 1                 # Add 1
                i -= 1
                while i >= msb:                         # Copy the rest
                    ans[i - msb] = A[i]
                    i -= 1
                return ans
    return ans

print plusOne(A)



