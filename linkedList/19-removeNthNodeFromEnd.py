# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # use the two pointers method, pointer 'first' preceeds 'second' by n+1 step
        # refer to solution Approach #2
        if head == None: return []
        # add a dummy node before head, deal with cases of deleting the first node
        d = ListNode(True)
        d.next = head
        # initialize two pointers
        first = second = d
        # first pointer preceed second by n+1 steps
        for i in range(n+1):
            first = first.next
        # move both first, second pointer until first reaches None
        while first != None:
            first = first.next
            second = second.next
        # remove the element
        second.next = second.next.next
        return d.next
            
