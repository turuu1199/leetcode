# Definition for singly-linked list.
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

        num1 = ''
        num2 = ''
        sum = 0
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next


        num1Array = list(map(int, str(num1)))
        num2Array = list(map(int, str(num2)))

        num1reversed = num1Array[::-1]
        num2reversed = num2Array[::-1]

        num1 = ''
        num2 = ''
        for i in num1reversed:
            num1 += str(i)

        for i in num2reversed:
            num2 += str(i)

        sum = int(num1) + int(num2)

        arraySum = list(map(int, str(sum)))

        arrayReversed = arraySum[::-1]

        head = ListNode()
        current = head

        for i in arrayReversed:
            current.next = ListNode(i)
            current = current.next
        
        node = head.next

        return node

# testNode = ListNode()

# testNode = ListNode(0)
# testNode.next = ListNode(5)

# print(testNode.val)
# print(testNode.next.val)

list1 = [2,4,3]
list2 = [5,6,4]

head = ListNode()
carry = head

for i in list1:
    carry.next = ListNode(i)
    carry = carry.next

l1 = head.next

head = ListNode()
carry = head

for i in list2:
    carry.next = ListNode(i)
    carry = carry.next

l2 = head.next


sol = Solution()

sol.addTwoNumbers(l1,l2)