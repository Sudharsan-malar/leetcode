class Solution:
    def merge(self, intervals):
        intervals.sort()  # sort by start time
        
        merged = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            
            if start <= last_end:  # overlap
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])
        
        return merged