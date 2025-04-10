from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        dummy = ListNode(0, head)
        prev_group_end = dummy

        while True:
            # 检查是否有足够的节点进行翻转
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            group_start = prev_group_end.next
            next_group_start = kth_node.next

            # 翻转当前组
            prev, curr = None, group_start
            while curr != next_group_start:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # 连接翻转后的链表
            prev_group_end.next = kth_node
            group_start.next = next_group_start
            prev_group_end = group_start
# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print()
k=2
solution = Solution()
result = solution.reverseKGroup(head, k)
while result:
    print(result.val, end=" -> ")
    result = result.next