class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [float('-inf')] * len(nums)
        dp[0] = nums[0]
        
        prevMax = dp[0]
        prevMin = dp[0]

        for i in range(1, len(nums)):
            print('prevMin', prevMin)
            print('prevMax', prevMax)
            dp[i] = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            tempPrevMin = prevMin
            prevMin = min(nums[i] * prevMin, nums[i], nums[i] * prevMax)
            prevMax = max(nums[i] * prevMax, nums[i], nums[i] * tempPrevMin)  
            # prev in changes so i need temp var  

        return max(dp)

# [2, -5, -2, -4, 3]