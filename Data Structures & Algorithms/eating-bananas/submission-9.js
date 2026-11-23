class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let left = 1 
        let right = Math.max(...piles)

        while(left < right){
            const k = Math.floor((left + right) / 2)
            let sum = 0
            for(const bananas of piles){
                sum += Math.ceil(bananas / k)
            }       

            if(sum <= h){
                right = k
            }else{
                left = k + 1
            }
        }
        
        return left 
    }
}
