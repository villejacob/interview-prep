'''
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1 or not l2:
            return l1 or l2

        head = current = ListNode(0)

        ## ITERATIVE
        #while l1 and l2:
        #    if l1.val < l2.val:
        #        current.next = l1
        #        l1 = l1.next
        #    else:
        #        current.next = l2
        #        l2 = l2.next
        #    current = current.next
        #current.next = l1 or l2
        #return head.next

        # RECURSIVE
        def recursiveMerge(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = recursiveMerge(l1.next, l2)
                return l1
            else:
                l2.next = recursiveMerge(l1, l2.next)
                return l2
        #return recursiveMerge(l1, l2)

        ## ITERATIVE IN PLACE
        head.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = current.next
                current.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            current = current.next
        current.next = l1 or l2
        return head.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(8)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(5)
list2.next.next.next = ListNode(6)
list2.next.next.next.next = ListNode(7)

result = Solution().mergeTwoLists(list1, list2) 
res = []
while result:
    res.append(result.val)
    result = result.next
print res
