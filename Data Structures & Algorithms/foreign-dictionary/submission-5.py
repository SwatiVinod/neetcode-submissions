from collections import deque, defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        graph = defaultdict(list)
        indegree = {}

        for word in words:
            for ch in word:
                indegree[ch] = 0

        # Build graph
        for i in range(1, n):
            word1 = words[i-1]
            word2 = words[i]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for j in range(min(len(word1), len(word2))):
                c1 = word1[j]
                c2 = word2[j]
                if c1 != c2:
                    graph[c1].append(c2)
                    break
        print(graph)

        # Build indegree dict
        for node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1
        print(indegree)

        queue = deque()

        for char, value in indegree.items():
            if value == 0:
                queue.append(char)

        # Perform BFS
        result = []
        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbour in graph[char]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(result) < len(indegree):
            return ""

        return "".join(result)

        