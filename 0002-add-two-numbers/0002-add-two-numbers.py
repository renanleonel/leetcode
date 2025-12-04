# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2:
            sumVal = 0

            if not l1:
                sumVal = l2.val + carry
                l2 = l2.next
            elif not l2:
                sumVal = l1.val + carry
                l1 = l1.next
            else:
                sumVal = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next

            remainder = sumVal % 10
            carry = sumVal // 10

            head.next = ListNode(remainder)
            head = head.next

        if carry != 0:
            head.next = ListNode(carry)

        return dummy.next