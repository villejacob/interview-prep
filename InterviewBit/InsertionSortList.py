'''
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insert(self, head, value):
        # If the value will replace the head
        if value < head.val:
            new_head = ListNode(value)
            new_head.next = head
            return new_head
        past = head
        current = head
        while current and current.val < value:
            past = current
            current = current.next
        past.next = ListNode(value)
        past.next.next = current
        return head

    def insertionSortList(self, A):

        # If A is None return A
        if not A:
            return A

        head = A
        past = A
        current = past.next

        while current:
            if past.val > current.val:
                # Skip over current
                past.next = current.next
                # Insert current into the list
                head = self.insert(head, current.val)
                current = past.next
            else:
                past = current
                current = current.next

        return head













head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(1)
soln = Solution()
sorted = soln.insertionSortList(head)
# inserted = soln.insert(head, 5.5)
current = sorted
while current:
    print current.val, "->",
    current = current.next
print None
