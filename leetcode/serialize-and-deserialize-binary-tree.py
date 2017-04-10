'''
Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in the
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no
restriction on how your serialization/deserialization algorithm should work. You
just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
    
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary
tree. You do not necessarily need to follow this format, so please be creative
and come up with different approaches yourself.
'''                                  
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        serialized = []
        q = deque([root])
        while q:
            for i in xrange(len(q)):
                n = q.popleft()
                if n:
                    serialized.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
                else:
                    serialized.append(n)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        parents, children = [root], []
        i = 0
        while parents:
            for p in parents:
                if p:
                    if i < len(data)-1 and data[i+1] is not None:
                        p.left = TreeNode(data[i+1])
                        children.append(p.left)
                    if i < len(data)-2 and data[i+2] is not None:
                        p.right = TreeNode(data[i+2])
                        children.append(p.right)
                    i += 2
            parents, children = children, []
        return root

    def printTreeInorder(self, root):
        if not root:
            return
        self.printTreeInorder(root.left)
        print root.val,
        self.printTreeInorder(root.right)


root0 = TreeNode(1)
root0.left = TreeNode(2)
root0.right = TreeNode(3)
root0.right.left = TreeNode(4)
root0.right.right = TreeNode(5)
root0.right.left.right = TreeNode(6)

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right = TreeNode(3)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)

root2 = TreeNode(-1)
root2.left = TreeNode(0)
root2.right = TreeNode(1)

codec = Codec() 
codec.printTreeInorder(codec.deserialize(codec.serialize(root2)))
