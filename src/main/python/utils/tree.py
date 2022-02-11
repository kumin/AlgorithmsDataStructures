from typing import List, Optional


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val


def BuildBinTree(vals: List[int]) -> Optional[TreeNode]:
    n = len(vals)
    if n == 0:
        return
    nodes = []
    for i in range(n):
        if vals[i] != None:
            nodes.append(TreeNode(val=vals[i]))
        else:
            nodes.append(None)
    j = 0
    for i in range(n):
        if not nodes[i]:
            continue
        if j * 2 + 1 < n:
            nodes[i].left = nodes[j * 2 + 1]
        if j * 2 + 2 < n:
            nodes[i].right = nodes[j * 2 + 2]
        j+=1
    return nodes[0]


def InorderTraversal(root: Optional[TreeNode]):
    if not root:
        return
    InorderTraversal(root.left)
    print(root.val)
    InorderTraversal(root.right)


if __name__ == '__main__':
    root = BuildBinTree([5, 4, 1, None, 1, None, 4, 2, None, 2, None])
    InorderTraversal(root)
