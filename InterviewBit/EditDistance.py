'''
Given two words A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example :
edit distance between
"Anshuman" and "Antihuman" is 2.

Operation 1: Replace s with t.
Operation 2: Insert i.
'''

class Solution:
    # @return an integer
    def minDistance(self, s1, s2):
        if len(s1) == 0 and len(s2) == 0: return 0
        if len(s1) == 0: return len(s2)
        if len(s2) == 0: return len(s1)
        D = [[]] * (len(s1) + 1)
        for x in range(len(s1) + 1): D[x] = [0] * (len(s2) + 1)
        for x in range(len(s2) + 1): D[0][x] = x
        for x in range(len(s1) + 1): D[x][0] = x
        for x in range(1,len(s1)+1):
            for y in range(1,len(s2)+1):
                if s1[x-1] == s2[y-1]: D[x][y] = min(D[x-1][y-1], D[x][y-1] + 1, D[x - 1][y] + 1)
                else: D[x][y] = min(D[x-1][y-1] + 1,D[x][y - 1] + 1, D[x - 1][y] + 1)
        return D, D[len(s1)][len(s2)]


soln = Solution()
ans, edit = soln.minDistance('aababbabb', 'bbbaabaa')
print edit
for x in xrange(len(ans)):
    print ans[x]
