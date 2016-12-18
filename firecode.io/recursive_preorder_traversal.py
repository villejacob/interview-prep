class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def validate_BST_Itr(self, root):
        if not root:
            return False
        if root.left_child:
            return self.search(root.left_child, None, root.data)
        if root.right_child:
            return self.search(root.right_child, root.data, None)

    def search(self, root, min, max):
        print root.data, min, max
        if min:
            if root.data <= min:
                return False
        if max:
            if root.data >= max:
                return False
        if not root.left_child and not root.right_child:
            return
        if root.left_child:
            if root.left_child.data >= root.data:
                return False
            return self.search(root.left_child, min, root.data)
        if root.right_child:
            if root.right_child.data <= root.data:
                return False
            return self.search(root.right_child, root.data, max)
        return True

root = TreeNode(20)
root.left_child = TreeNode(15)
root.right_child = TreeNode(40)
root.left_child.left_child = TreeNode(10)
root.left_child.right_child = TreeNode(30)
test_tree = BinaryTree(root)

print test_tree.validate_BST_Itr(root)