from utils.tree import TreeNode, BuildBinTree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def DFS(lt: TreeNode, rt: TreeNode) -> bool:
            if lt == rt == None:
                return True
            if (not lt and rt) or (lt and not rt) or (lt.val != rt.val):
                print(lt.val, rt.val)
                return False
            return DFS(lt.left, rt.right) and DFS(lt.right, rt.left)

        return DFS(root.left, root.right)


if __name__ == '__main__':
    vals = [1,2,2,3,4,4,3]
    root = BuildBinTree(vals)
    sol = Solution()
    print(sol.isSymmetric(root))
