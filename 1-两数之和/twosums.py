# -*- coding: utf-8 -*-


# 先固定一个数x，之后我们就知道了另一个数的大小，再查找在列表里是否存在这个数
# 我们把数组的值作为键值，构建一个哈希表，可以在常数时间内查找列表里是否存在这个数
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 构建哈希表
        # hashmap = dict()
        # for i, x in enumerate(nums):
        #     hashmap[x] = i
        # for i, x in enumerate(nums):
        #     y = target - x
        #     if hashmap.has_key(y):
        #         k = hashmap[y]
        #         if k != i:
        #             return [i, k]

        # 解法2，边插入边检查
        hashmap = dict()
        for i, x in enumerate(nums):
            y = target - x
            if hashmap.has_key(y):
                k = hashmap[y]
                if k != i:
                    return [i, k]
            hashmap[x] = i

if __name__ == '__main__':
    s = Solution()
    res1 = s.twoSum([2, 7, 11, 15], 9)
    res2 = s.twoSum([2, 7, 11, 15, 30], 45)
    res3 = s.twoSum([2, 7, 11, 15, 0], 4)
    res4 = s.twoSum([3,3], 6)

    print res