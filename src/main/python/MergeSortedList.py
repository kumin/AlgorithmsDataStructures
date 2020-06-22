# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return None

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l1
        if l1.val >= l2.val:
            l3 = l2

        return None
