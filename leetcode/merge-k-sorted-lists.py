'''
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
'''
from heapq import heapify, heapreplace, heappop

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        head = merged = ListNode(0)
        h = [(node.val, node) for node in lists if node]
        heapify(h)
        while h:
            val, node = h[0]
            if node.next:
                heapreplace(h, (node.next.val, node.next))
            else:
                heappop(h)
            merged.next = node
            merged = merged.next
        return head.next

list1 = ListNode(2)
list1.next = ListNode(3)
list1.next.next = ListNode(4)
list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(12)
list3 = ListNode(5)
list3.next = ListNode(7)
list3.next.next = ListNode(8)
list4 = ListNode(4)
list4.next = ListNode(5)
node_list = [list1, list2, list3, list4]

result = Solution().mergeKLists(node_list)
res = []
while result:
    res.append(result.val)
    result = result.next
print res
