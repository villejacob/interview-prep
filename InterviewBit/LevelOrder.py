'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
Also think about a version of the question where you are asked to do a level
order traversal of the tree when depth of the tree is much greater than number
of nodes on a level.
'''
import collections

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        import collections
    	level_queue = collections.deque()
    	level_queue.append(A)
    	output_list = []
    	level_list = []
    	level_vals = []
    	while level_queue:
    		while level_queue:
    		    node = level_queue.popleft()
    		    level_list.append(node)
    		    level_vals.append(node.val)
    		for node in level_list:
    			if node.left:
	    			level_queue.append(node.left)
	    		if node.right:
	    			level_queue.append(node.right)
    		output_list.append(level_vals)
    		level_list = []
    		level_vals = []
    	return output_list


# Test Tree Initiation
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
# Run Test Case
soln = Solution()
result = soln.levelOrder(root)

for val in result:
	print val

