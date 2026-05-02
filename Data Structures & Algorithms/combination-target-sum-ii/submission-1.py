class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        

        def backtrack(start, state, currentAmount):
            if currentAmount == target: 
                result.append(state[:])
                return

            if currentAmount > target:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]

                if i > start and candidate == candidates[i-1]:
                    continue

                state.append(candidate)
                backtrack(i + 1, state, currentAmount + candidate)
                state.pop()

        backtrack(0, [], 0)

        return result