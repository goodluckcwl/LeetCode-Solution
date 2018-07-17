# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        # 首先判断根节点，如果根节点不满足，则删除根节点，更换根节点
        # 接着分别对子树递归调用

        # 空树
        if not root:
            return root
        if root.val > R or root.val < L:
            # 寻找新的根节点
            while root:
                if root.val > R:
                    root = root.left
                elif root.val < L:
                    root = root.right
                else:
                    break
        else:
            pass

        # 分别对左右子树操作
        if root:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)

        return root

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(5)
    r1 = s.trimBST(t1, L=4, R=5)

    print ''
