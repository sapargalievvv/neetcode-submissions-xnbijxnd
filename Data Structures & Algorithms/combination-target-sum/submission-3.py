class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(start, remaining, state):
            if remaining == 0:
                res.append(state[:])
                return 
            elif remaining < 0:
                return

            for i in range(start, len(nums)):
                state.append(nums[i])
                bt(i, remaining - nums[i], state)
                state.pop()

        
        bt(0, target, [])

        return res