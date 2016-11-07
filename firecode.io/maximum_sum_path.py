class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # All the necessary collection moduled have been already imported.
    def max_sum_path(self, root):

        if not root:
            return 0

        def max_sub(root):

            if not root:
                return 0

            if root.left_child and root.right_child:
                lr_max = max(max_sub(root.left_child), max_sub(root.right_child))
                return root.data + lr_max
            elif root.left_child:
                return root.data + max_sub(root.left_child)
            elif root.right_child:
                return root.data + max_sub(root.right_child)
            else:
                return root.data

        return max_sub(root.left_child) + root.data + max_sub(root.right_child)


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_8 = TreeNode(8)
node_9 = TreeNode(9)

node_1.left_child = node_2; node_1.right_child = node_3
node_2.left_child = node_4; node_2.right_child = node_5
node_3.left_child = node_6; node_3.right_child = node_7
node_4.left_child = node_8; node_4.right_child = node_9

bin_tree = BinaryTree(node_1)

print bin_tree.max_sum_path(bin_tree.root)