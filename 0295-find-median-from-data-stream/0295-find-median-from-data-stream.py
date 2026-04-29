import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (invert values)
        self.large = []  # min heap

    def addNum(self, num):
        # Step 1: push to max heap
        heapq.heappush(self.small, -num)
        
        # Step 2: move largest of small → large
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: balance sizes (small can have 1 extra)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0