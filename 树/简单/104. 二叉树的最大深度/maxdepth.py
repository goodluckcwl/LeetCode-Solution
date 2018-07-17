# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 等于左子树的深度与右子树的深度的最大值，加上1
        if not root:
            return 0

        if root.left or root.right:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        else:
            return 1

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    r0 = s.maxDepth(t1)
    t1.left = TreeNode(2)
    r1 = s.maxDepth(t1)
    t1.right = TreeNode(3)
    r2 = s.maxDepth(t1)
    t1.left.left = TreeNode(4)
    r3 = s.maxDepth(t1)

    print ''