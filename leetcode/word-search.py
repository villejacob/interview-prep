'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example,
Given board =

[   ['A','B','C','E'], 
    ['S','F','C','S'], 
    ['A','D','E','E']   ]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(i, j, word, 0, board):
                    return True
        return False

    def dfs(self, i, j, word, index, board):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i == len(board) or j == len(board[0]):
            return False
        if word[index] != board[i][j]:
            return False
        board[i][j] = '#'
        ret =      self.dfs(i, j-1, word, index+1, board) \
                or self.dfs(i, j+1, word, index+1, board) \
                or self.dfs(i-1, j, word, index+1, board) \
                or self.dfs(i+1, j, word, index+1, board)
        board[i][j] = word[index]
        return ret


board = [['A','B','C','E'], 
         ['S','F','C','S'], 
         ['A','D','E','E']]
board2 = [['B']]
board3 = [['A','B','C','E'],
          ['S','F','E','S'],
          ['A','D','E','E']]
print "True:", Solution().exist(board, "ABCCED")
print "True:", Solution().exist(board, "SEE")
print "False:", Solution().exist(board, "ABCB")
print "False:", Solution().exist(board2, "A")
print "True:", Solution().exist(board2, "B")
print "True:", Solution().exist(board3, "ABCESEEEFS")
