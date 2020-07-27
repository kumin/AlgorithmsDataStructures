# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            curr = root.right

            while curr.right:
                curr = curr.right
            curr.right = temp


if __name__ == '__main__':
    solution = Solution()
    leaf1 = TreeNode(3)
    leaf2 = TreeNode(4, TreeNode(7, None, None), TreeNode(8, None, None))
    leaf3 = TreeNode(6)
    node1 = TreeNode(2, leaf1, leaf2)
    node2 = TreeNode(5, None, leaf3)
    node_root = TreeNode(1, node1, node2)

    solution.flatten(node_root)
    node = node_root
    while node:
        print(node.val)
        node = node.right
