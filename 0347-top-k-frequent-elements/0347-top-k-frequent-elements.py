class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        
        count = Counter(nums)              # frequency map
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]