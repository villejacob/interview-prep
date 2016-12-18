import collections, sys

class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self, root_node = None):
		self.root = root_node
    
    def validate_BST_Itr(self,root):

    	class RangeNode:
    		def __init__(self, tree_node, node_min, node_max):
    			self.node = tree_node
    			self.min = node_min
    			self.max = node_max

    	root_node = RangeNode(root, -sys.maxint-1, sys.maxint)
    	deck = collections.deque()
    	deck.append(root_node)
    	while deck:
    		current = deck.pop()
    		if current.node:
    			if current.min and current.node.data < current.min:
    				return False
    			if current.max and current.node.data > current.max:
    				return False
    			deck.append(RangeNode(current.node.left_child, current.min, current.node.data))
    			deck.append(RangeNode(current.node.right_child, current.node.data, current.max))
    	return True


root_node = TreeNode(20, TreeNode(17, TreeNode(10), TreeNode(18)), TreeNode(30))
test_tree = BinaryTree(root_node)
print test_tree.validate_BST_Itr(test_tree.root)