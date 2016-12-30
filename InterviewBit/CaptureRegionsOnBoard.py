'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

# class Solution:
#     # @param A : list of list of chars

#     def identifyOs(self, A):
#     	# Generate empty 2D matrix of size A
#     	enclosed_block_id = [[0 for val in A[0]] for val in xrange(len(A))]
#     	enclosed_id = 1
# 		# Flag each O with a unique number
#     	for i, row in enumerate(A):
#     		for j, col in enumerate(row):
#     			if A[i][j] == 'O':
#     				enclosed_block_id[i][j] = enclosed_id
#     				enclosed_id += 1
#     	return enclosed_block_id

#     def generateBlocks(self, A, enclosed_block_id):
#     	enclosed_blocks = {}
# 		# If above, below, left, or right are O, take the smallest ID
#     	for i, row in enumerate(A):
#     		for j, col in enumerate(row):
#     			if enclosed_block_id[i][j] != 0:
#     				min_id = enclosed_block_id[i][j]
#     				if i > 0 and enclosed_block_id[i-1][j] != 0:
#     					min_id = min(min_id, enclosed_block_id[i-1][j])
#     				if j > 0 and enclosed_block_id[i][j-1] != 0:
#     					min_id = min(min_id, enclosed_block_id[i][j-1])
#     				if i < len(A)-1 and enclosed_block_id[i+1][j] != 0:
#     					min_id = min(min_id, enclosed_block_id[i+1][j])
#     				if j < len(A[0])-1 and enclosed_block_id[i][j+1] != 0:
#     					min_id = min(min_id, enclosed_block_id[i][j+1])
#     				enclosed_block_id[i][j] = min_id
#     				# If the block id does not exist, add location to dictionary
#     				if min_id in enclosed_blocks:
# 	    				enclosed_blocks[min_id].append([i, j])
#     				else:
#     					enclosed_blocks[min_id] = [[i, j]]
#     	return enclosed_blocks

#     def verifyEnclosed(self, enclosed_block_id, enclosed_blocks):
#     	for key, val in enclosed_blocks.items():
#     		for location in enclosed_blocks[key]:
#     			i, j = location
#     			# If the O lies on a boundary, remove from dictionary
#     			if i == 0 \
#     				or j == 0 \
#     				or i == len(enclosed_block_id)-1 \
#     				or j == len(enclosed_block_id[0])-1: 
#     				enclosed_blocks[key] = []
#     	return enclosed_blocks

#     def createResult(self, enclosed_block_id, enclosed_blocks):
#     	for i, row in enumerate(enclosed_block_id):
#     		for j, col in enumerate(row):
#     			# Output X if 0 or in enclosed_blocks
#     			if enclosed_block_id[i][j] == 0 \
#     				or len(enclosed_blocks[enclosed_block_id[i][j]]) > 0:
#     				enclosed_block_id[i][j] = 'X'
#     			else:
#     				enclosed_block_id[i][j] = 'O'


#     def solve(self, A):

#     	# Flag each O with a unique ID
#     	enclosed_block_id = self.identifyOs(A)
#     	# Identify regions of connected Os with unique ID
#     	enclosed_blocks = self.generateBlocks(A, enclosed_block_id)
#     	# Check if these regions are surrounded by an X
#     	enclosed_blocks = self.verifyEnclosed(enclosed_block_id, enclosed_blocks)
#     	# Modify the matrix with enclosed regions
#     	self.createResult(enclosed_block_id, enclosed_blocks)

#     	return enclosed_block_id

# Attempt no.2
class Solution:
    # @param A : list of list of chars


    def uncapturedDFS(self, A, row, col):
    	# Perform DFS on edge O and mark all connected O's as +
        A[row][col] = '+'
        # Look up (if not top row)
        if row > 0 and A[row-1][col] == 'O':
            A = self.uncapturedDFS(A, row-1, col)
        # Look down (if not bottom row)
        if row < len(A)-1 and A[row+1][col] == 'O':
            A = self.uncapturedDFS(A, row+1, col)
        # Look left (if not left column)
        if col > 0 and A[row][col-1] == 'O':
            A = self.uncapturedDFS(A, row, col-1)
        # Look right (if not right column)
        if col < len(A[0])-1 and A[row][col+1] == 'O':
            A = self.uncapturedDFS(A, row, col+1)
        return A


    def flagRim(self, A):
    	# Identify Os on the top and bottom borders of the matrix
        for top_col, top in enumerate(A[0]):
            if top == 'O':
    			A = self.uncapturedDFS(A, 0, top_col)
    	for bottom_col, bottom in enumerate(A[-1]):
            if bottom == 'O':
    			A = self.uncapturedDFS(A, len(A)-1, bottom_col)
    	# Flag O's on the left and right hand borders
    	for left_row in xrange(len(A)):
            if A[left_row][0] == 'O':
    			A = self.uncapturedDFS(A, left_row, 0)
        for right_row in xrange(len(A)):
            if A[right_row][-1] == 'O':
    			A = self.uncapturedDFS(A, right_row, len(A[0])-1)
        return A


    def convert(self, A):
        for i, row in enumerate(A):
            for j, value in enumerate(row):
                if value == '+':
                    A[i][j] = 'O'
                if value == 'O':
                    A[i][j] = 'X'
        return A


    def solve(self, A):	
    	# Find regions of O's that are not enclosed
    	A = self.flagRim(A)
    	# Format output to indicate whether region is enclosed
    	A = self.convert(A)
    	return A


soln = Solution()
test_board = [	['O', 'X', 'X', 'X', 'O'], \
                ['X', 'O', 'O', 'O', 'X'], \
                ['X', 'X', 'O', 'X', 'X'], \
                ['O', 'O', 'X', 'O', 'X'], \
                ['O', 'X', 'X', 'X', 'O'] ]

result = soln.solve(test_board)

for row in result:
    for char in row:
        print char,
    print