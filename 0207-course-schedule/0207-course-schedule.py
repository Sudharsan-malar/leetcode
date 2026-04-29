from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        
        # Build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # Start with courses having no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        
        while queue:
            node = queue.popleft()
            count += 1
            
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count == numCourses