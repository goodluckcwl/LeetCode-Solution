# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 找到数组的中间节点作为根节点，再构造左子树和右子树

        N = len(nums)
        if N == 0:
            return None

        idx = N/2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST(nums[0:idx])
        if idx == N - 1:
            root.right = None
        else:
            root.right = self.sortedArrayToBST(nums[idx + 1:])
        return root

if __name__ == '__main__':
    s = Solution()
    t1 = s.sortedArrayToBST([-10,-3,0,5,9])

    print ''