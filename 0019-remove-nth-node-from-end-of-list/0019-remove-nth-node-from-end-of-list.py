# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = self.reverseLL(head)

        i = 1
        prev, curr = None, head

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

        head = self.reverseLL(head)
        return head