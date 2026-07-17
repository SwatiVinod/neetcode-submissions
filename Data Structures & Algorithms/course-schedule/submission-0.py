from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for second, first in prerequisites:
            indegree[first] += 1
            adj[second].append(first)
        
        print(indegree)
        print(adj)
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        finish = 0
        while queue:
            curr = queue.popleft()
            finish += 1
            for neighbour in adj[curr]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        return finish == numCourses

        