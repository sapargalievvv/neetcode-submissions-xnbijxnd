class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (right + left) // 2 
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile / k)

            if hrs <= h:
                right = k
            else:
                left = k + 1

        return left
            