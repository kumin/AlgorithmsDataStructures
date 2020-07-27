# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root):

        def dfs(root, count=0):
            if not root: return 0
            count ^= 1 << (root.val - 1)
            res = dfs(root.left, count) + dfs(root.right, count)
            if root.left == root.right:
                if count & (count - 1) == 0:
                    res += 1
            return res

        return dfs(root)


if __name__ == '__main__':
    solution = Solution()
    root = [2, 3, 1, 3, 1, None, 1]
    leaf1 = TreeNode(3)
    leaf2 = TreeNode(1)
    leaf3 = TreeNode(1)
    node1 = TreeNode(3, leaf1, leaf2)
    node2 = TreeNode(1, None, leaf3)
    node_root = TreeNode(2, node1, node2)

    print((solution.pseudoPalindromicPaths(node_root)))
