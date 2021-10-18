# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        return self.DFS(root, targetSum) + self.pathSum(root.right, targetSum) + self.pathSum(root.left, targetSum)

    def DFS(self, node: TreeNode, sum: int) -> int:
        if node is None:
            return 0
        return (1 if node.val == sum else 0) + self.DFS(node.right, sum - node.val) + self.DFS(node.left,
                                                                                               sum - node.val)


if __name__ == '__main__':
    sol = Solution()
    vals = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    nodes = []
    for i in range(len(vals)):
        if vals[i] is None:
            nodes.append(None)
        else:
            nodes.append(TreeNode(vals[i]))
    root = nodes[0]
    for i in range(len(nodes) // 2):
        if i * 2 + 1 < len(nodes):
            nodes[i].left = nodes[i * 2 + 1]
        if i * 2 + 2 < len(nodes):
            nodes[i].right = nodes[i * 2 + 2]

    print(sol.pathSum(root, 8))
