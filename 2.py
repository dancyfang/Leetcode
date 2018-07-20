# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Let's add a comment here.
        root = n = ListNode(0) # copy root, shallow copy
        carry = 0
        while l1 or l2 or carry: 
            v1 = v2 = 0 # handle None value
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry,10)
            n.next = ListNode(val) # if we use: n.val = ListNode(val) n.next = ListNode(0) n = n.next   we might get an extra 0 before result
            n = n.next
        return root.next 
# add a comment here
