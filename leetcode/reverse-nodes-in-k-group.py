'''
Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
'''
from linkedlist import *

class Solution(object):
    def reverseKIndex(self, head, k):
        # Reverses nodes before an index
        if not head or k == 1: return head
        new_head = head
        for i in xrange(1, k):
            new_head = new_head.next
            if not new_head: return head
        prev = current = head
        next = current.next
        while next and next is not new_head:
            current = next
            next = next.next
            current.next = prev
            prev = current
        head.next = new_head.next
        new_head.next = current
        return new_head

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or k == 1: return head
        
        oldh = newh = nextt = head
        while nextt:
            for i in xrange(1, k):
                newh = newh.next
                if not newh: 
                    return head

            if oldh is head: head = newh
            else: oldh.next = newh

            prev = current = nextt
            next = current.next
            while next and next is not newh:
                current = next
                next = next.next
                current.next = prev
                prev = current
            nextt.next = newh.next
            newh.next = prev
            oldh = nextt
            nextt = nextt.next
            newh = nextt

        return head

list4 = createLinkedList(xrange(1, 5))
printList(list4)
printList(Solution().reverseKGroup(list4, 2))
