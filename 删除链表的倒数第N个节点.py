# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        # Move both pointers until first reaches the end
        while first:
            first = first.next
            second = second.next
        # Remove the nth node from the end
        second.next = second.next.next
        return dummy.next
# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
solution = Solution()
result = solution.removeNthFromEnd(head, n)
while result:
    print(result.val, end=" -> ")
    result = result.next
