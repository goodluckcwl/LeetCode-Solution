# -*- coding: utf-8 -*-
import math

class Solution(object):
    def is_prime(self, x):
        if x == 1:
            return False

        for i in range(2, int(math.sqrt(x))+1, 1):
            if x % i == 0:
                return False
        return True

    def is_palindrome(self, x):

        if x == 0:
            return True
        r = []
        while x:
            r.append( x % 10)
            x = x/10
        for i,v in enumerate(r):
            if r[-1-i] != v:
                return False
        return True



    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = N
        while True:
            if self.is_palindrome(x):
                if self.is_prime(x):
                    return x
            x += 1

if __name__ == '__main__':
    s = Solution()
    r0 = s.primePalindrome(9989900)
    r1 = s.primePalindrome(1000)
    print ''