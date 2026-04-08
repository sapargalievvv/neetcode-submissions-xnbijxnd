class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, state, currentSum): 
            if currentSum > target or start == len(nums):
                return 

            if currentSum == target: 
                result.append(state[:]) 
                return

            for i in range(start, len(nums)):
                candidate = nums[i]
                state.append(candidate)

                backtrack(i, state, currentSum + candidate)
                
                state.pop()

        backtrack(0, [], 0)

        return result