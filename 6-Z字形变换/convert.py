# -*- coding: utf-8 -*-

# 我们

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        N = len(s)
        rstr = [0] * N
        k = 0
        # 步长，当numRows=1的时候是1，其他时候是0
        step = 1 if numRows == 1 else (numRows - 2) * 2 + 2
        for i in range(numRows):
            # 初始值
            idx = i
            if idx < N:
                rstr[k] = s[idx]
                k = k + 1
            else:
                break
            # 另一个步长
            step1 = (numRows - i - 2) * 2 + 2
            while True:
                if i < numRows - 1 and i > 0:
                    if idx + step1 < N:
                        rstr[k] = s[idx + step1]
                        k = k + 1
                    else:
                        break

                idx = idx + step
                if idx < N:
                    rstr[k] = s[idx]
                    k = k + 1
                else:
                    break
            if k >= N:
                break
        return ''.join(rstr)




if __name__ == '__main__':
    s = Solution()
    #
    re0 = s.convert('PAYPALISHIRING', numRows=3)
    re1 = s.convert('abcdefghijklmnopqrst', numRows=3)
    re2 = s.convert('abcdefghijklmnopqrst', numRows=2)
    # abcdefghijklmnopqrst
    re3 = s.convert('abcdefghijklmnopqrst', numRows=100)
    # abcdefghijklmnopqr ts
    re4 = s.convert('abcdefghijklmnopqrst', numRows=19)
    re5 = s.convert('PAYPALISHIRING', numRows=4)
    re6 = s.convert('', numRows=1)
    re7 = s.convert('Abcde', 1)
    print 'done'