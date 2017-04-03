'''
Find the largest sum of the values within consecutive nodes.

0 0 0 2
2 2 0 4     ->  returns 10 (2+4+3+1)
0 0 1 3         note: 2+2 is also a valid island
'''

def dfs(i, j, grid, visited, cur):
    """
    :type i,j,cur: int
    :type grid: list[list[int]]
    :type grid: list[list[bool]]
    :rtype: int 
    """
    r = len(grid)
    c = len(grid[0])
    # visited after tuple to prevent indexing out of range
    if True in (i < 0, j < 0, i >= r, j >= c) or visited[i][j]:
        return 0
    visited[i][j] = True
    up = dfs(i, j+1, grid, visited, cur)
    down = dfs(i, j-1, grid, visited, cur)
    left = dfs(i-1, j, grid, visited, cur)
    right = dfs(i+1, j, grid, visited, cur)
    return grid[i][j] + up + down + left + right


def largestIsland(grid):
    """
    :type grid" list[list[int]]
    :rtype: int
    """
    if not grid: return -1
    r = len(grid)
    c = len(grid[0])
    visited = [[True if g==0 else False for g in l] for l in grid]
    # Sets to min int to allow negative island values
    max_island = -2**31 - 1
    for i in xrange(r):
        for j in xrange(c):
            if not visited[i][j]:
                max_island = max(max_island, dfs(i, j, grid, visited, 0))
    return max_island


grid = [[0, 1, 0, 2],
        [1, 0, 2, 6],
        [0, 1, 0, 0]]
print largestIsland(grid)
