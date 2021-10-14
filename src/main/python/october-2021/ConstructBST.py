# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        for i in range(1, len(preorder)):
            cn = root
            while True:
                if cn.val > preorder[i]:
                    if cn.left is None:
                        cn.left = TreeNode(val=preorder[i])
                        break
                    cn = cn.left
                else:
                    if cn.right is None:
                        cn.right = TreeNode(val=preorder[i])
                        break
                    cn = cn.right

        return root



if __name__ == '__main__':
    sol = Solution()
    print(sol.bstFromPreorder([8, 5, 1, 7, 10, 12]))
