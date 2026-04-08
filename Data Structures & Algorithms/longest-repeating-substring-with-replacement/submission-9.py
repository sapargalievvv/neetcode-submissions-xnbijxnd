class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        res = 0
        letters = {}
        max_freq = 0

        while right < len(s):
            char = s[right]
            letters[char] = letters.get(char, 0) + 1
            max_freq = max(max_freq, letters[char])


            while (right - left + 1) - max_freq > k:
                letters[s[left]] -= 1
                left += 1

            res = max(right - left + 1, res)
            right += 1 
            

        return res


# 1 берем char
# 2 window size 
# 3 count max freq 