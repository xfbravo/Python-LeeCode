# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev=dummy
        current=head
        #如果当前节点和下一个节点都不为空
        while current and current.next:
            #如果当前节点和下一个节点都不为空，那么就交换当前节点和下一个节点
            prev.next=current.next
            temp=current.next.next
            current.next.next=current
            current.next=temp
            prev=current
            current=current.next
        return dummy.next
# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
result = solution.swapPairs(head)
while result:
    print(result.val, end=" -> ")
    result = result.next
