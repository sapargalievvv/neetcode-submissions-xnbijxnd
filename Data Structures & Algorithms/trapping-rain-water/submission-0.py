class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        res = 0

        while left < right:
            if height[left] < height[right]:
                waterAmount = leftMax - height[left]
                if waterAmount > 0:
                    res += waterAmount

                leftMax = max(leftMax, height[left])
                left+=1
            else:
                waterAmount = rightMax - height[right]
                if waterAmount > 0:
                    res += waterAmount
                    
                rightMax = max(rightMax, height[right])
                right -= 1
        
        return res
            