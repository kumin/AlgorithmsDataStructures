# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        cousins = [False]
        dx = [0]
        def DFS(node: TreeNode, deep: int) -> int:
            if node is None or cousins[0]:
                return -1
            if node.val == x or node.val == y:
                return deep
            dl = DFS(node.left, deep + 1)
            dr = DFS(node.right, deep + 1)
            if dl == dr != -1 and dr - deep > 1:
                cousins[0] = True
            return max(-1, dl, dr)

        DFS(root, 0)
        return cousins[0]


if __name__ == '__main__':
    sol = Solution()
    vals = [1, 2, 3, None, 4]
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

    print(sol.isCousins(root, 2, 3))
