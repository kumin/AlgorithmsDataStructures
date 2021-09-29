# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        head_nodes = [None] * k
        current_nodes = [None] * k
        node = head
        i = 0
        while node is not None:
            if head_nodes[i] is None:
                head_nodes[i] = node
                current_nodes[i] = node
            else:
                current_nodes[i].next = node
                current_nodes[i] = node
            tem = node.next
            node.next = None
            node = tem
            i += 1
            if i >= k:
                i = 0

        return head_nodes

