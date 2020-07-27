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

        flatten_node = [root]

        def dfs(root: TreeNode, flatten_node: List[TreeNode]):
            if root.left:
                flatten_node.append(root.left)
                dfs(root.left, flatten_node)
            if root.right:
                flatten_node.append(root.right)
                dfs(root.right, flatten_node)

        dfs(root, flatten_node)
        for i in range(len(flatten_node) - 1):
            flatten_node[i].right = flatten_node[i + 1]
            flatten_node[i].left = None
        node = root
        while node:
            print(node.val)
            node = node.right


if __name__ == '__main__':
    solution = Solution()
    leaf1 = TreeNode(3)
    leaf2 = TreeNode(4)
    leaf3 = TreeNode(6)
    node1 = TreeNode(2, leaf1, leaf2)
    node2 = TreeNode(5, None, leaf3)
    node_root = TreeNode(1, node1, node2)

    solution.flatten(None)
