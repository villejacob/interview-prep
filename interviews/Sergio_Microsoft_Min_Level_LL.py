class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class LinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None

from Queue import Queue
from sys import maxint

def LevelMinLinkedList(tree_root):

    q = Queue()
    q.put(tree_root)

    list_head = None
    current_list_node = None

    while not q.empty():

        level = q.qsize()
        level_min = maxint

        for parent in xrange(level):

            current = q.get()

            level_min = min(current.value, level_min)

            if current.left:
                q.put(current.left)
            if current.right:
                q.put(current.right)

        if not list_head:
            list_head = LinkedNode(level_min)
            current_list_node = list_head

        else:
            current_list_node.next = LinkedNode(level_min)
            current_list_node = current_list_node.next

    return list_head

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

linked_list_head = LevelMinLinkedList(root)

while linked_list_head:
    print linked_list_head.value
    linked_list_head = linked_list_head.next