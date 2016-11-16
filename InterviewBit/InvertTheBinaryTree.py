'''
Given a binary tree, invert the binary tree and return it.
Look at the example for more details.

Example :
Given binary tree

     1
   /   \
  2     3
 / \   / \
4   5 6   7
invert and return

     1
   /   \
  3     2
 / \   / \
7   6 5   4

'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @return the root node in the tree
    def invertTree(self, root):

        def invert(tree_node):
            if not tree_node:
                return
            tree_node.left, tree_node.right = tree_node.right, tree_node.left
            invert(tree_node.left)
            invert(tree_node.right)
            return

        invert(root)
        return root

    def printTreeInorder(self, root):
        if not root:
            return
        self.printTreeInorder(root.left)
        print root.val,
        self.printTreeInorder(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

soln = Solution()
inverted = soln.invertTree(root)
soln.printTreeInorder(inverted)
