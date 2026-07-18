class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        graph = [[] * n for _ in range(n)]
        for node, neighbour in edges:
            graph[node].append(neighbour)
            graph[neighbour].append(node)
        traversal = set()

        def dfs(node, parent):
            if node in traversal:
                return False

            traversal.add(node)

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
            
        
        result = dfs(0, -1)
        return result and len(traversal) == n

        