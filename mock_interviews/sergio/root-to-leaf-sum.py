'''
Return a list of all nodes in a path from the root to leaf that equal the sum
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rootToLeafSum(self, root, sum):
        ret, current = [], []
        self.checkPath(root, sum, current, ret)
        return ret

    def checkPath(self, root, remaining, current, ret):
        if not root: return

        remaining -= root.val
        current.append(root.val)

        if not root.left and not root.right:
            if remaining == 0:
                ret.append(current[:])
            current.pop()
            return

        self.checkPath(root.left, remaining, current, ret)
        self.checkPath(root.right, remaining, current, ret)
        current.pop()

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
res = Solution().rootToLeafSum(root, 22)
for e in res:
    print e
