'''
You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;
Example :

Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]

Output : 5
         With 10 from A, 15 from B and 10 from C.
'''

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        import sys

        # Initialize pointers to beginning of each array
        i, j, k = [0] * 3

        min_diff = sys.maxint
        found = False

        while not found:
            current_max = max(A[i], B[j], C[k])
            current_min = min(A[i], B[j], C[k])
            # Update the global minimum difference if current is smaller
            min_diff = min(min_diff, current_max - current_min)
            # If A is the min and not the last of A, increment i
            if B[j] >= A[i] <= C[k] and i < len(A) - 1:
                i += 1
            # If B is the min and not the last of B, increment j
            elif A[i] >= B[j] <= C[k] and j < len(B) - 1:
                j += 1
            # If C is the min and not the last of C, increment k
            elif A[i] >= C[k] <= B[j] and k < len(C) - 1:
                k += 1
            # Exit when no min or all are at the last element
            else:
                found = True

        return min_diff


A1 = [1, 2, 5, 8, 12]
B1 = [4, 12, 13, 18]
C1 = [1, 2, 3, 5, 15]
soln = Solution()
print soln.minimize(A1, B1, C1)
