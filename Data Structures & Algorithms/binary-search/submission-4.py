import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            print(mid)
            
            if nums[mid] == target:
                return mid

            if nums[mid] > target: 
                right -= 1

            if nums[mid] < target: 
                left += 1

        return -1
