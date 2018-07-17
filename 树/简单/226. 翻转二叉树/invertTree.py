# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 先把左右子树交换，再分别对左右子树进行操作

        # 空树直接返回
        if not root:
            return root

        node = root.left
        root.left = root.right
        root.right = node
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        return root

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    r1 = s.invertTree(t1)

    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    r2 = s.invertTree(t1)
    print ''