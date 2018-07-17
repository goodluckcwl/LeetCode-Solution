# -*- coding: utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s:str
        :rtype: str
        """
        rstr = []
        N = len(s)
        for i, x in enumerate(s):
            for j in range(min(N - 1 - i, i) + 1):
                if s[i + j] == s[i - j]:
                    if len(rstr) < len(s[i - j:i + j + 1]):
                        rstr = s[i - j:i + j + 1]
                else:
                    break
            # 另一种情况
            for j in range(min(i+1, N - i - 1)):
                if s[i - j] == s[i + 1 + j]:
                    if len(rstr) < len(s[i - j: i +1 +j + 1]):
                        rstr = s[i-j:i+1+j+1]
                else:
                    break
        return rstr

    def longestPalindrome2(self, s):
        """
        O(N)
        :param s:
        :return:
        """
        N = len(s)
        P = [0] * (2 * N + 1)
        largest_idx = 0
        for i in enumerate(2 * N + 1):
            # P[0]=0,P[1]=1
            if i <= 1:
                P[i] = i
            else:

            if P[i] > P[largest_idx]




if __name__ == '__main__':
    s = Solution()
    r0 = s.longestPalindrome('aabb')
    # bcdcb
    r1 = s.longestPalindrome('abcdcbx')
    # bcb, bacab,cbacabc
    r2 = s.longestPalindrome('abcbacabc')
    #
    r3 = s.longestPalindrome('aaaaaaa')
    #
    r4 = s.longestPalindrome('abcde')

