class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        res = 0
        window_vals = set()

        while right < len(s):
            if s[right] in window_vals:
                window_vals.remove(s[left])
                left += 1 
            else:
                window_vals.add(s[right])
                res = max(res, right - left + 1)
                right += 1

        return res 