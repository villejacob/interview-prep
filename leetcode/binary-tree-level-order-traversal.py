'''
Given a binary tree, return the level order traversal of its nodes' values. (ie,
        from left to right, level by level).

For example: Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its level order traversal as:
    [
        [3],
        [9, 20],
        [15, 7]
    ]
'''
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_order = []
        q = deque([root])
        count = 1
        while q:
            level = []
            for i in xrange(count):
                n = q.popleft()
                if n:
                    level.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if level: level_order.append(level)
            count = len(q)
        return level_order


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.left.left = TreeNode(4)
r1.right = TreeNode(3)
r1.right.left = TreeNode(5)
r1.right.right = TreeNode(6)
r1.right.right.left = TreeNode(7)
r1.right.right.right = TreeNode(8)
r1.right.right.right.left = TreeNode(9)
r1.right.right.right.left.right = TreeNode(10)

res = Solution().levelOrder(rr1)
for row in res:
    print row
