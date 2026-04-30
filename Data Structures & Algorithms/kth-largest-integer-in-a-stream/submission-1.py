class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.arr = nums[:]
        self.k = k

        heap_size = len(nums)

        for i in range(heap_size // 2 - 1, -1, -1):
            self.min_heapify(self.arr, len(self.arr), i)

        while len(self.arr) > k:
            self.pop_min()

    def add(self, val: int) -> int:
        
        if len(self.arr) < self.k:
            self.arr.append(val)
            self.bubble_up(len(self.arr) - 1)
        elif val > self.arr[0]:
            self.arr[0] = val
            self.min_heapify(self.arr, len(self.arr), 0)
        
        return self.arr[0]


    def bubble_up(self, i):

        while i > 0:
            parent_ind = (i - 1) // 2
            parent = self.arr[parent_ind]

            if parent > self.arr[i]:
                self.arr[parent_ind], self.arr[i] = self.arr[i], self.arr[parent_ind]
                i = parent_ind
            else:
                break

    def pop_min(self):
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        if len(self.arr) > 0:
            self.min_heapify(self.arr, len(self.arr), 0)

    def min_heapify(self, arr, size, i):
        l = i * 2 + 1
        r = i * 2 + 2

        smallest = i

        if l < size and arr[smallest] > arr[l]:
            smallest = l

        if r < size and arr[smallest] > arr[r]:
            smallest = r

        if smallest != i:
            (
                arr[smallest],
                arr[i],
            ) = arr[i], arr[smallest]
            self.min_heapify(arr, size, smallest)
