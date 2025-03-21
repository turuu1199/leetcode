# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        n1 = ListNode()
        for i in l1:
            n1.next = i
            n1.next            

        while n1.next != None:
            print(n1.next)
            n1.next
n1 = ListNode()


l1 = [2,4,3]
l2 = [5,6,4]

sol = Solution()
sol.addTwoNumbers(l1, l2)

