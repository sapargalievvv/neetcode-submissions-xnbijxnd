class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        digits = set()
        
        for num in nums:
            if num in digits:
                return True
            digits.add(num)

        return False