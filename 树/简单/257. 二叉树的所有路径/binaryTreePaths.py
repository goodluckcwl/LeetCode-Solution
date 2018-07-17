# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 遍历:左->右->根节点
        if not root:
            return []
        path = []

        path += self.binaryTreePaths(root.left)
        path += self.binaryTreePaths(root.right)

        # 叶子节点
        if not root.left and not root.right:
            path.append(str(root.val))
        # 非叶子节点
        else:
            for i, p in enumerate(path):
                path[i] = '{}->{}'.format(root.val, path[i])

        return path

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(5)
    r1 = s.binaryTreePaths(t1)
    print ''