from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = [0]

        def DFS(node: TreeNode, depth: List[int]) -> None:
            print(node.val)
            val = node.val
            d_left = [0]
            if node.left is not None:
                d_left[0] = 1
                DFS(node.left, d_left)
            d_right = [0]
            if node.right is not None:
                d_right[0] = 1
                DFS(node.right, d_right)
            if d_left[0] + d_right[0] > max_path[0]:
                max_path[0] = d_left[0] + d_right[0]
            depth[0] += max(d_left[0], d_right[0])

        DFS(root, [0])
        return max_path[0]


if __name__ == '__main__':
    sol = Solution()
    t = [1, 2]
    tree = []
    for i in range(len(t)):
        tree.append(TreeNode(t[i]))
    for i in range(len(tree) // 2):
        tree[i].left = tree[2 * i + 1]
        if 2 * i + 2 < len(tree):
            tree[i].right = tree[2 * i + 2]
    print(sol.diameterOfBinaryTree(tree[0]))
