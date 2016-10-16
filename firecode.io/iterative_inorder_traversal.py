class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def inorder_iterative(self):
        inorder_list = []
        root = self
        stack = []

        # Go as far left as you can, adding nodes to the stack (Create L of LVR)
        while root:
            stack.append(root)
            root = root.left_child

        # Take a node, append L then V to the list, go right when possible
        while stack:
            root = stack.pop()
            inorder_list.append(root.data)
            root = root.right_child

            # Go as far left as possible at this right child
            while root:
                stack.append(root)
                root = root.left_child

        return inorder_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data