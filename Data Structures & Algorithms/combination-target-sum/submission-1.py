class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, amount, state):
            if amount > target or start == len(nums):
                return

            if amount == target:
                result.append(state[:])
                return

            for i in range(start, len(nums)):
                candidate = nums[i]
                state.append(candidate)
                backtrack(i, amount + candidate, state)
                state.pop()

        backtrack(0, 0, [])

        return result
