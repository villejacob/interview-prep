'''
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
'''

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # Approach: interleave clones between original allowing 
        #           the reference without hashing

        if not head: return head
        current = head
        while current:
            next = current.next
            current.next = RandomListNode(current.label)
            current.next.next = next
            current = next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        current = head
        clone_head = RandomListNode(0)
        copy = current_copy = clone_head
        while current:
            next = current.next.next
            copy = current.next
            current_copy.next = copy
            current_copy = copy
            current.next = next
            current = next
        return clone_head.next
        

    def printRandomList(self, head):
        cur = head
        while cur:
            print "Node: ", cur.label, "\tNext: ", 
            if cur.next: print cur.next.label, "\tRandom: ",
            else: print "None", "\tRandom: ",
            if cur.random: print cur.random.label
            else: print "None"
            cur = cur.next
        print


node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node4 = RandomListNode(4)
node5 = RandomListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node1.random = node3
node2.random = node5
node3.random = node2
node4.random = node1
node5.random = node4
n1 = RandomListNode(1)
n2 = RandomListNode(2)
n1.next = n2
n1.random = n2.next
n2.random = n1
n3 = RandomListNode(3)
Solution().printRandomList(node1)
clone = Solution().copyRandomList(node1)
Solution().printRandomList(clone)
