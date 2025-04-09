# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#                链表1                   链表2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #最后的结果
        l3_result=ListNode(0)
        l3=l3_result#结果链表的指针
        #如果链表1和链表2都不为空
        while l1 is not None and l2 is not None:
            l3.val+=l1.val+l2.val#更新链表3
            #如果链表1或者链表2还有下一个节点，那么链表3一定存在下一个节点
            if l1.next is not None or l2.next is not None:
                l3.next=ListNode(0)#创建一个新的节点
            #如果链表3的值大于等于10，那么就要进位，那么就要减去10，并且链表3的下一个节点设置为1
            #这样能保证链表3的下一个节点一定存在，即使链表1和链表2都没有下一个节点
            if l3.val>=10:
                l3.val-=10
                l3.next=ListNode(1)
            #更新链表3和链表1和链表2的指针
            l3=l3.next
            l1=l1.next
            l2=l2.next
        #如果链表1不为空，链表2为空，那么就要把链表1的值加到链表3上，原理和上面一样
        while l1 is not None:
            l3.val+=l1.val
            if l1.next is not None:
                l3.next=ListNode(0)
            if l3.val>=10:
                l3.val-=10
                l3.next=ListNode(1)
            l3=l3.next
            l1=l1.next
        #如果链表2不为空，链表1为空，那么就要把链表2的值加到链表3上，原理和上面一样
        while l2 is not None:
            l3.val+=l2.val
            if l2.next is not None:
                l3.next=ListNode(0)
            if l3.val>=10:
                l3.val-=10
                l3.next=ListNode(1)
            l3=l3.next
            l2=l2.next
        return l3_result
# Example usage:
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)
while l3:
    print(l3.val, end=" -> ")
    l3 = l3.next
