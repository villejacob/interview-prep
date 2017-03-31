def findLargest(matrix):
    print len(matrix[0]), len(matrix)
    print matrix[0][3]
    max_int = -2**31
    gbl_max = max_int
    memo = [[False for i in xrange(len(matrix[0]))] for j in
            xrange(len(matrix))]
    for i in xrange(len(matrix[0])):
        for j in xrange(len(matrix)):
            if matrix[i][j] != 0 and not memo[i][j]:
                gbl_max = max(gbl_max, dfs(i, j, memo, matrix, max_int))
    return gbl_max

def dfs(i, j, memo, matrix, max):
    if matrix[i][j] != 0:
        max += matrix[i][j]
    memo[i][j] = True
    print i, j
    if i < len(matrix[0])-1 and matrix[i+1][j] != 0 and not memo[i+1][j]:
        dfs(i+1, j, memo, matrix, max)
    if i > 0 and matrix[i-1][j] != 0 and not memo[i-1][j]:
        dfs(i-1, j, memo, matrix, max)
    if j < len(matrix)-1 and matrix[i][j+1] != 0 and not memo[i][j+1]:
        dfs(i, j+1, memo, matrix, max)
    if j > 0 and matrix[i][j-1] != 0 and not memo[i][j-1]:
        dfs(i, j-1, memo, matrix, max)
    return max

m = [   [0, 0, 0, 2],
        [1, 3, 0, 4],
        [0, 0, 1, 3]   ]

print findLargest(m)
