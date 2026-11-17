class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2
            time_sum = 0
            
            for pile in piles:
                time_sum += math.ceil(pile / k)

            if time_sum <= h:
                right = k
            else:
                left = k + 1

        return left
