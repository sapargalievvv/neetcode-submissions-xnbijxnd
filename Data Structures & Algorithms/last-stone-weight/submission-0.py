
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def maxheap(arr,size,i):
            largest = i

            l = i * 2 + 1 
            r = i * 2 + 2

            if l < size and arr[l] > arr[largest]:
                largest = l
            if r < size and arr[r] > arr[largest]:
                largest = r
            if i != largest:
                arr[largest], arr[i] = arr[i], arr[largest]
                maxheap(arr,size,largest)

        def buildheap(arr):
            heapsize = len(arr)

            for i in range(heapsize // 2 - 1, -1, -1):
                maxheap(arr, heapsize, i)

        buildheap(stones)

        def popMax(arr):
            maximum = arr[0]
            arr[0] = arr[-1]
            arr.pop()

            if len(arr) > 0:
                maxheap(arr, len(arr), 0)
            
            return maximum


        print(stones)
        while len(stones) > 1:
            s1 = popMax(stones)
            s2 = popMax(stones)

            diff = s1 - s2

            if diff > 0:
                stones.append(diff)
                buildheap(stones)

        return stones[0] if len(stones) > 0 else 0
        

