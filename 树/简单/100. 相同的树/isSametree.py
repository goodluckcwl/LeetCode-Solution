# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 判断根是否相同，左子树、右子树是否相同
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        else:
            if p.val != q.val:
                return False
            if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
            else:
                return False

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(5)
    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(4)
    r1  = s.isSameTree(t1, t2)
    print ''