# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        result = lists[0]
        for i in range(1, len(lists)):
            result = self.merge2Lists(result, lists[i])
        return result

    def merge2Lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = l1
        if (not l1 and l2) or (l1 and l2 and l1.val >= l2.val):
            l3 = l2
            l2 = l2.next
        elif l1:
            l1 = l1.next
        firstNode = l3
        while l1 or l2:
            if (not l1 and l2) or (l2 and l1 and l1.val >= l2.val):
                l3.next = l2
                l3 = l2
                l2 = l2.next
            elif l1:
                l3.next = l1
                l3 = l1
                l1 = l1.next

        return firstNode

    def genListNode(self, d: List) -> ListNode:
        firstNode = ListNode(d[0])
        temNode = firstNode
        for i in range(1, len(d)):
            nextNode = ListNode(d[i])
            temNode.next = nextNode
            temNode = nextNode

        return firstNode

    def iterateListNode(self, l: ListNode):
        while l:
            print(l.val)
            l = l.next


if __name__ == '__main__':
    d1 = [1, 4, 5]
    d2 = [1, 3, 4]
    d3 = [2, 6]

    solution = Solution()
    l1 = solution.genListNode(d1)
    l2 = solution.genListNode(d2)
    l3 = solution.genListNode(d3)

    ls = [None, None]
    solution.iterateListNode(solution.mergeKLists(ls))
