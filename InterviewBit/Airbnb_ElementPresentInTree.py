class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None


def isPresent(root, val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not

    # If the root is None
    if not root:
        return 0

    # If the node is found
    if root.value == val:
        return 1

    # If the value is smaller than (or equal to) the current node value, go left
    if val <= root.value:
        if root.left:
            return isPresent(root.left, val)

    # If the value is greater than the current node value, go right
    else:
        if root.right:
            return isPresent(root.right, val)

    return 0

