# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        # 保存每一层的所有节点，用于获取下一层所有节点
        # 当没有节点的时候停止计算
        nodes_cur = [root]
        levels = []
        while nodes_cur:
            val = 0
            nodes_tmp = []
            for node in nodes_cur:
                val += node.val
                if node.left:
                    nodes_tmp.append(node.left)
                if node.right:
                    nodes_tmp.append(node.right)
            levels.append(val/1.0/len(nodes_cur))
            nodes_cur = nodes_tmp
        return levels

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)
    t1.left.right = TreeNode(5)

    r1 = s.averageOfLevels(t1)
    print ''