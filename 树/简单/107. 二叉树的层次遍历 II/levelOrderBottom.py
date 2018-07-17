# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 逐层遍历，每次保留该层的节点，取出下层的节点，直到所有节点都处理完
        res_lst = []
        if not root:
            return []
        nodes_cur = [root]
        while nodes_cur:
            val_lst = []
            nodes_tmp = []
            for node in nodes_cur:
                val_lst.append(node.val)
                if node.left:
                    nodes_tmp.append(node.left)
                if node.right:
                    nodes_tmp.append(node.right)
            nodes_cur = nodes_tmp
            res_lst.append(val_lst)
        return res_lst[::-1]

if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.right.right = TreeNode(4)
    t1.right.right.right = TreeNode(5)
    r1 = s.levelOrderBottom(t1)
    print ''