# -*- coding: utf-8 -*-
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # 1.合并根节点
        # 2.合并左右子树
        if t1 and t2:
            t1.val = t1.val + t2.val
            # 合并子树
            if t1.left and t2.left:
                self.mergeTrees(t1.left, t2.left)
            if not t1.left and t2.left:
                t1.left = t2.left
            if t1.left and not t2.left:
                pass

            if t1.right and t2.right:
                self.mergeTrees(t1.right, t2.right)
            if not t1.right and t2.right:
                t1.right = t2.right
            if t1.right and not t2.right:
                pass

            return t1
        if t1 and not t2:
            return t1
        if not t1 and t2:
            t1 = t2
            return t1





if __name__ == '__main__':
    s = Solution()
    # Create trees
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.left.left = TreeNode(5)
    t1.right = TreeNode(2)
    #
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    t3 = s.mergeTrees(t1, t2)
    print ''