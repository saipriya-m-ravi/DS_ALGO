# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, A, B):
        dummy = ListNode(-1)
        dummy.next = A
        slow = dummy
        fast = dummy

        for _ in range(B+1):
            fast = fast.next
            if not fast:
                return A.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
