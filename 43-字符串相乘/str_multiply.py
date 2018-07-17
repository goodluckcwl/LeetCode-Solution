# -*- coding: utf-8 -*-
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0]
        num1 = [int(n) for n in num1]
        num2 = [int(n) for n in num2]
        if num1[0] == 0 or num2[0] == 0:
            return '0'

        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                m = n1 * n2
                carry = m / 10
                r = m % 10
                if len(res) > i+j:
                    s = res[i+j] + r
                    carry = carry + s / 10
                    res[i+j] = s % 10
                else:
                    res.append(r)
                # 逐级进位
                carry_idx = i + j + 1
                while(carry > 0):
                    if len(res) > carry_idx:
                        s = res[carry_idx] + carry
                        carry = s / 10
                        res[carry_idx] = s % 10
                        carry_idx = carry_idx + 1
                    else:
                        res.append(carry)
                        carry = 0


        num3 = ''
        for x in res[::-1]:
            num3 = num3 + str(x)
        return num3

def main():
    import sys

    ret6 = Solution().multiply('123','456')
    ret1 = Solution().multiply('1', '0')
    ret2 = Solution().multiply('0', '1')
    ret3 = Solution().multiply('0', '0')
    ret4 = Solution().multiply('1000000000000', '2')
    ret5 = Solution().multiply('1000000000000', '2000000000000000000')
    print ret5


if __name__ == '__main__':
    main()