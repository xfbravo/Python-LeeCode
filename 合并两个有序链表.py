# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(0)
        current=head
        #遍历两个链表
        while list1 and list2:
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        #如果链表1还有剩余，就把链表1的剩余部分接到链表3上
        if list1:
            current.next=list1
        #如果链表2还有剩余，就把链表2的剩余部分接到链表3上
        if list2:
            current.next=list2
        return head.next
solution = Solution()
# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
result = solution.mergeTwoLists(list1, list2)
while result:
    print(result.val, end=" -> ")
    result = result.next
