# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first, second = head, head.next
        while second and second.next:
            first = first.next
            second = second.next.next

        then = first.next
        prev = first.next = None
        while then:
            tmp = then.next
            then.next = prev
            prev = then
            then = tmp
        
        second = prev
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2