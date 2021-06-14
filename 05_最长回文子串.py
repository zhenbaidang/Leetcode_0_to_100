# O(n^3) 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n)的一个判断s_str字符串是否是回文串的函数
        def isPalindrome(s_str):
            n = len(s_str)
            if n == 1:
                return True
            for i in range(n//2):
                if s_str[i] == s_str[n-1-i]:
                    continue
                else:
                    return False
            return True
        n = len(s)
        max_len = 0
        result = ''
        # 遍历所有字符串子串，判断是否为回文串，如果是，且长度大于已有最大值，则更新最大值，并保存这个子串到result中
        for i in range(n):
            for j in range(i+1, n+1):
                if isPalindrome(s[i:j]) and (len(s[i:j]) > max_len):
                    max_len = len(s[i:j])
                    result = s[i:j]
                
        return result
    
