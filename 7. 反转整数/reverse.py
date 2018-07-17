# -*- coding: utf-8 -*-

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 统一转成正数处理
        if x < 0:
            flag = -1
            # 判断是否越界
            if x <= - pow(2, 31):
                return 0
            x = -x
        elif x > 0:
            flag = 1
        else:
            return 0

        l = []

        while x/10 or x%10:
            # 余数
            r = x % 10
            # 商
            x = x/10
            l.append(r)
        y = 0
        valid_n = 0
        for i, r in enumerate(l):
            if valid_n >=10:
                return 0
            if valid_n == 9 and y > 214748364:
                return 0
            if valid_n == 9 and y == 214748364:
                if r>8 and flag == -1:
                    return 0
                if r>7 and flag == 1:
                    return 0

            if y == 0 and r == 0:
                pass
            else:
                valid_n += 1
            y = y * 10 + r

        return y if flag>0 else -y



if __name__ == '__main__':
    s = Solution()
    r6 = s.reverse(-2147483412)
    r0 = s.reverse(0)
    r1 = s.reverse(-1)
    r2 = s.reverse(1)
    r3 = s.reverse(-100)
    # 0
    r4 = s.reverse(-pow(2, 31))
    # 0
    r5 = s.reverse(pow(2,31) - 1)
    # 214748365

    print 'Done'