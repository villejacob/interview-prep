'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def pathSum(self, root, sum1):

        self.paths = []

        # When the root has a left child, start the path as the root
        if root.left:
            self.checkPath(root.left, sum1, root.val, [root.val])

        # When the root has a right child, start the path as the root
        if root.right:
            self.checkPath(root.right, sum1, root.val, [root.val])

        return self.paths

    def checkPath(self, root, target, current, path):

        # Base case: when the root is a leaf, and the sum with its parent is the target sum
        if not root.left and not root.right and target == current + root.val:
            # Append the current value to the path stored in pathSum, then return the final path
            self.paths.append(path + [root.val])
            return

        # When there is a left child, keep track of the new sum, add this node's value to the path
        if root.left:
            self.checkPath(root.left, target, current + root.val, path + [root.val])

        # When there is a right child, keep track of the new sum, add this node's value to the path
        if root.right:
            self.checkPath(root.right, target, current + root.val, path + [root.val])


# For testing: X_Y: X is the level (starting at 1) and Y is the node in the row (starting 1)
root1_1 = TreeNode(5)
root2_1 = TreeNode(4); root2_2 = TreeNode(8)
root3_1, root3_2, root3_3 = TreeNode(11), TreeNode(13), TreeNode(4)
root4_1, root4_2, root4_3, root4_4 = TreeNode(7), TreeNode(2), TreeNode(5), TreeNode(1)


                                                                #           5
                                                                #          / \
                                                                #         /   \
root1_1.left = root2_1; root1_1.right = root2_2                 #        4     8
                                                                #       /     / \
root2_1.left = root3_1                                          #      11    /   \
root2_2.left = root3_2; root2_2.right = root3_3                 #     / \   13    4
                                                                #    /   \       / \
root3_1.left = root4_1; root3_1.right = root4_2                 #   7     2     /   \
root3_3.left = root4_3; root3_3.right = root4_4                 #              5     1

mySolution = Solution()
print mySolution.pathSum(root1_1, 22)
