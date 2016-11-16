'''
Given a positive integer n,
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        sieve = []
        i = 1

        # Create list of all perfect squares that are in the range of n: O(n)
        while i*i < n:
            sieve.append(i*i)
            i += 1

        count = 0

        # Check is a set of the current sum (n)
        # As a set it allows no duplicate values
        check = {n}
        while check:
            # Increment the counter
            count += 1
            # Create a temporary set to contain sum - square values
            temp = set()
            # for each of the resulting sums
            for sum in check:
                # for each square in the sieve
                for square in sieve:
                    # return if goal reached
                    if square == sum:
                        return count
                    # Exit the loop if adding a square will exceed the sum
                    if sum < square:
                        break
                    # Subtract the square from the sum and add to the set
                    temp.add(sum-square)
            # Complete this again for each of the unique decremented sums
            check = temp
        return count


soln = Solution()
print soln.numSquares(144)