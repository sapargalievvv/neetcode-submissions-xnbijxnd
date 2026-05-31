class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        left = 0

        for i in range(len(prices)):
            profit = prices[i] - prices[left]
            res = max(res, profit)

            if prices[left] > prices[i]:
                left = i
        
        return res 