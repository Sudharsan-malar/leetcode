class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        result = ""
        
        for i in range(len(s)):
            # Odd length palindrome
            p1 = expand(i, i)
            # Even length palindrome
            p2 = expand(i, i+1)
            
            result = max(result, p1, p2, key=len)
        
        return result