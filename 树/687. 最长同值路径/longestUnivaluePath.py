# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


if __name__ == '__main__':
    s = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(4)
    t1.right = TreeNode(5)
    t1.left.right = TreeNode(4)
    t1.left.left = TreeNode(4)
    t1.right.left = TreeNode(5)
    r1 = s.longestUnivaluePath(t1)
    print ''