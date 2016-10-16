'''
Merge k sorted linked lists and return it as one sorted list.

Example :

1 -> 10 -> 20
4 -> 11 -> 13
3 -> 8 -> 9
will result in

1 -> 3 -> 4 -> 8 -> 9 -> 10 -> 11 -> 13 -> 20
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):

        import heapq

        # Set head to point to the heap
        head = ListNode(0)

        # Declare pointer to keep track of last node in the list
        current = head
        heap = []

        # Create a heap with k heads from the list A
        for sortedList in A:
            heapq.heappush(heap, (sortedList.val, sortedList))

        # As long as there in an element in the heap
        while heap:

            # Takes the smallest value in the heap
            smallest = heapq.heappop(heap)[1]

            # Set the next pointer in the current node of the list to point to this
            current.next = smallest

            # Set current to be this new node
            current = current.next

            # If the element taken was the head of a list
            if smallest.next:

                # Push the next node in that list onto the heap
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        # Return head's next to get the first element from A, since head was created by me
        return head.next

# Create list from example used in the problem description
head1 = ListNode(1)
head1.next = ListNode(10)
head1.next.next = ListNode(20)
head2 = ListNode(4)
head2.next = ListNode(11)
head2.next.next = ListNode(13)
head3 = ListNode(3)
head3.next = ListNode(8)
head3.next.next = ListNode(9)

headList = [head1, head2, head3]

mySolution = Solution()
ansHead = mySolution.mergeKLists(headList)

# Prints out the list in an easy to read format
while ansHead:
    print "{0}" .format(ansHead.val),
    if ansHead.next:
        print "->",
    ansHead = ansHead.next