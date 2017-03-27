class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createLinkedList(val_list):
    head = prev = ListNode(0)
    for val in val_list:
        prev.next = ListNode(val)
        prev = prev.next
    return head.next

def printList(head):
    current = head
    while current:
        print current.val, "->",
        current = current.next

list1 = createLinkedList(xrange(1, 6))
list2 = createLinkedList(xrange(2, 13, 2))
list3 = createLinkedList(xrange(1, 10))
