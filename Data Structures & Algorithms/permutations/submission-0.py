class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, state):
            if start == len(nums):
                result.append(state[:])
                return
            
            for i in range(len(nums)):
                num = nums[i]

                if num in state:
                    continue

                state.append(num)

                backtrack(start+1, state)

                state.pop()

        backtrack(0, [])
        
        return result
            