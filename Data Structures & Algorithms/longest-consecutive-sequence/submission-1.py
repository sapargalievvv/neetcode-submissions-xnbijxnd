class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)

        for num in numset: 
            if num - 1 not in numset: 
                length = 1
                current = num 
                
                while current + 1 in numset:
                    length += 1
                    current += 1

                longest = max(longest, length)

        return longest


