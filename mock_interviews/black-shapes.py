'''
Given N * M field of O's and X's, where O=white, X=black
Return the number of black shapes. A black shape consists of one or more
adjacent X's (diagonals not included)

Example: answer is 3 shapes:
                i  ii  iii
    OOOXOOO     X   X   X
    OOXXOXO    XX       X
    OXOOOXO


Note that we are looking for connected shapes
'''

class Solution:
    def dfs(self, i, j, A, visited):

        n = len(A)
        m = len(A[0])
        if i<0 or j<0 or i>=n or j>=m or visited[i][j]:
            return 0
        visited[i][j] = True
        up = self.dfs(i, j+1, A, visited)
        down = self.dfs(i, j-1, A, visited)
        left = self.dfs(i-1, j, A, visited)
        right = self.dfs(i+1, j, A, visited)
        return 1 + up + down + left + right

    def black(self, A):
        # @param A : list of strings
        # @return an integer

        if not A: return 0
        n = len(A)
        m = len(A[0])
        shapes = 0
        visited = [[True if a=='O' else False for a in l] for l in A]
        for i in xrange(n):
            for j in xrange(m):
                if not visited[i][j]:
                    if self.dfs(i, j, A, visited) > 0:
                        shapes += 1
        return shapes

print Solution().black(["OOXOOO", "OXXOXO", "OOOXOO"])
