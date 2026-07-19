class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)
        
        def find(node):
            if node == parent[node]:
                return node
            parent_node = find(parent[node])
            return parent_node

        def union(n1, n2):
            r1 = find(n1)
            r2 = find(n2)

            if r1 == r2:
                return False
            if rank[r1] <= rank[r2]:
                parent[r2] = r1
            elif rank[r2] > rank[r1]:
                parent[r1] = r2
            
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]