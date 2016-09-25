'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

 Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list. Note 2:
Usually the version often seen in the interviews is reversing the whole linked list which is obviously an easier version of this question.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):

        prev = A
        i = A
        j = i.next
        position = 0
        start = A
        end = A

        while j is not None:
            j = i.next
            if position < m:
                position += 1
                i = i.next
            elif position < n:
                start = i
                while position < n:
                    prev = i
                    i = j
                    j = j.next
                    i.next = prev
                    position += 1
