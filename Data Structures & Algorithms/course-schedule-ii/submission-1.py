from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()

        # Build the graph
        for course, pre_req in prerequisites:
            graph[pre_req].append(course)

        # Build indegree
        for i, pre_reqs in enumerate(graph):
            for pre_req in pre_reqs:
                indegree[pre_req] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        result = []
        
        # BFS
        while queue:
            course = queue.popleft()
            result.append(course)
            for dep in graph[course]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
        if len(result) == numCourses:
            return result
        else:
            return []
