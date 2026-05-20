from _heapq import heapify


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def calculateDistanceFromOrigin(x, y):
            return x**2 + y**2

        def bubble_up(i):
            while i > 0:
                parent = (i - 1) // 2
                parentDist, _ = heap[parent]
                currentDist, _ = heap[i]
                if parentDist > currentDist:
                    heap[parent], heap[i] = heap[i], heap[parent]
                    i = parent
                else:
                    break

        def addToHeap(val):
            heap.append(val)
            bubble_up(len(heap) - 1)

        def min_heapify(heap_size, heap, i):
            smallest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < heap_size and heap[smallest][0] > heap[left][0]:
                smallest = left

            if right < heap_size and heap[smallest][0] > heap[right][0]:
                smallest = right

            if smallest != i:
                heap[smallest], heap[i] = heap[i], heap[smallest]
                min_heapify(heap_size, heap, smallest)

        def extractMin():
            if len(heap) == 0:
                return None

            smallest = heap[0]
            last = heap.pop()

            if len(heap) != 0:
                heap[0] = last
                min_heapify(len(heap), heap, 0)

            return smallest

        for point in points:
            x, y = point
            distance = calculateDistanceFromOrigin(x, y)
            addToHeap((distance, point))

        result = []

        for _ in range(k):
            smallest = extractMin()
            if smallest:
                result.append(smallest[1])

        return result
