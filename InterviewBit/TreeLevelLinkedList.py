class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None

root1_1 = TreeNode(5)
root2_1 = TreeNode(4); root2_2 = TreeNode(8)
root3_1, root3_2, root3_3 = TreeNode(11), TreeNode(13), TreeNode(4)
root4_1, root4_2, root4_3, root4_4 = TreeNode(7), TreeNode(2), TreeNode(5), TreeNode(1)


                                                                #           5
                                                                #          / \
                                                                #         /   \
root1_1.left = root2_1; root1_1.right = root2_2                 #        4     8
                                                                #       /     / \
root2_1.left = root3_1                                          #      11    /   \
root2_2.left = root3_2; root2_2.right = root3_3                 #     / \   13    4
                                                                #    /   \       / \
root3_1.left = root4_1; root3_1.right = root4_2                 #   7     2     /   \
root3_3.left = root4_3; root3_3.right = root4_4                 #              5     1


import Queue

def levelLinkedList(root):

    q1 = q2 = Queue.Queue()
    q1.put(root)
    ans = []
    head = None
    temp = head

    while q1:

        current = q1.get()
        temp.next = ListNode(current.val)

        # If there is no head assign this node as the head
        if not head:
            head = temp

        temp = temp.next

        if current.left: q2.put(current.left)
        if current.right: q2.put(current.right)

        if not q1:
            q1 = q2
            q2 = Queue.Queue()
            ans.append(head)
            head = None

    return ans

print levelLinkedList(root1_1)