from utils.tree import TreeNode, BuildBinTree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        lt = []
        rt = []

        def LRR(node: TreeNode):
            if not node:
                return
            if not node.left and node.right:
                lt.append(None)
            else:
                LRR(node.left)
            lt.append(node.val)
            if not node.right and node.left:
                lt.append(None)
            else:
                LRR(node.right)

        def RRL(node: TreeNode):
            if not node:
                return
            print(node.val)
            if not node.right and node.left:
                rt.append(None)
            else:
                RRL(node.right)
            rt.append(node.val)
            if not node.left and node.right:
                rt.append(None)
            else:
                RRL(node.left)

        LRR(root.left)
        RRL(root.right)
        print(lt, rt)
        return lt == rt


if __name__ == '__main__':
    vals = [5, 4, 1, None, 1, None, 4, 2, None, 2, None]
    root = BuildBinTree(vals)
    sol = Solution()
    print(sol.isSymmetric(root))
