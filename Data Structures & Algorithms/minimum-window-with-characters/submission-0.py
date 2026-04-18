class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        window_counts = {}
        t_counts = {}

        for ltr in t:
            t_counts[ltr] = t_counts.get(ltr, 0) + 1

        have, need = 0, len(t_counts)
        res, min_window = [0, 0], float('inf')

        while r < len(s):
            c = s[r]

            if c in t_counts:
                window_counts[c] = window_counts.get(c, 0, ) + 1
                if window_counts[c] == t_counts[c]:
                    have += 1

            while have == need:
                if r - l + 1 < min_window:
                    min_window = r - l + 1
                    res = [l, r]

                left_char = s[l]

                if left_char in t_counts:
                    window_counts[left_char] -= 1
                    if window_counts[left_char] < t_counts[left_char]:
                        have -= 1

                l += 1

            r += 1

        l, r = res
        return s[l:r + 1] if min_window != float('inf') else ""