class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            twoStepsBack = dp[i-2] + cost[i]
            oneStepBack = dp[i-1] + cost[i]

            dp[i] = min(twoStepsBack, oneStepBack)
        
        return min(dp[len(cost) - 1], dp[len(cost) - 2])