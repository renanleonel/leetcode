# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        i = 1
        head, curr = prev, prev
        prev = None

        while curr:
            if i == n:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                break

            else:
                i+=1
                prev = curr
                curr = curr.next

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev