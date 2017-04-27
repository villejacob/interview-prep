'''
Reverse linked list

1 -> 2 -> 3 -> None

Modify to:
3 -> 2 -> 1 -> None
'''
from linkedlist import *

class Solution(object):
    def reverseList(self, head):
        if not head: return None
        previous = current = head
        next = head.next
        while next:
            current = next
            next = next.next
            current.next = previous
            previous = current
        head.next = None
        return current
        

printList(list1)
reversedListHead = Solution().reverseLinkedList(list1)
printList(reversedListHead)
