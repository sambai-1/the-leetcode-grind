# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def merge2Lists(headA, headB):
            ans = ListNode(0)
            tmp = ans

            while headA or headB:
                if not headA or not headB:
                    tmp.next = headA or headB
                    return ans.next
                elif headA.val < headB.val:
                    tmp.next = headA
                    headA = headA.next
                else:
                    tmp.next = headB
                    headB = headB.next
                tmp = tmp.next
            return ans.next

        if len(lists) < 2:
            return lists[0] if len(lists) == 1 else None
        
        length = len(lists)
        while length > 1:
            for i in range(length // 2):
                lists[i] = merge2Lists(lists[i * 2], lists[i * 2 + 1])
            if length % 2 == 1:
                lists[length // 2] = lists[length - 1]
                length = length // 2 + 1
            else:
                length = length // 2
        
        return lists[0]
        

        