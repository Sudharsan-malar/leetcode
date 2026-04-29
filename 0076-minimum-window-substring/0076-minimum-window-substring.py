class Solution:
    def minWindow(self, s, t):
        from collections import Counter
        
        if not s or not t:
            return ""
        
        count_t = Counter(t)
        window = {}
        
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in count_t and window[char] == count_t[char]:
                have += 1
            
            while have == need:
                # update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1
                
                # shrink window
                window[s[left]] -= 1
                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""