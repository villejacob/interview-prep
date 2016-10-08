'''
Given A, generate all structurally unique BST's (binary search trees) that store values 1...A.

Example :
Given A = 3, your program should return all 5 unique BST's shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

A = 4

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : integer
    # @return a list of TreeNode
    def generateTrees(self, A):

        # Call function that handles the recursion. Returns List of TreeNodes
        return self.branch(1, A)


    def branch(self, start, end):

        result = []

        # Bound handling
        if start > end:
            result.append(None)

        # Iterating through the entire list
        for i in xrange(start, end + 1):

            # Call function with list to the left of current value
            left = self.branch(start, i - 1)

            # Call function with list to the right of current value
            right = self.branch(i + 1, end)

            # For every value in the above called lists
            for leftVal in left:
                for rightVal in right:
                    # Define current node
                    current = TreeNode(i)
                    # Define node to the left of current, creating the left branch of the tree
                    current.left = leftVal
                    # Define node to the right of current, creating the right branch of the tree
                    current.right = rightVal
                    # Append the current to the answer to return
                    result.append(current)

        return result


