# -*- coding: utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digitdict = dict()
        digitdict['2'] = ['a','b','c']
        digitdict['3'] = ['d','e','f']
        digitdict['4'] = ['g','h','i']
        digitdict['5'] = ['j','k','l']
        digitdict['6'] = ['m','n','o']
        digitdict['7'] = ['p','q','r','s']
        digitdict['8'] = ['t','u','v']
        digitdict['9'] = ['w','x','y','z']

        res = []
        for s in digits:
            tmp = []
            # 对第一个数字
            if not res:
                res = digitdict[s]
                continue
            # 当前已经构造的所有字符串
            for r in res:
                # 对数字对应的字母
                for x in digitdict[s]:
                    tmp.append(r + x)
            res = tmp
        return res







if __name__ == '__main__':
    s = Solution()
    r1 = s.letterCombinations('23')
    r2 = s.letterCombinations('234')
    r3 = s.letterCombinations('432')
    print ''
