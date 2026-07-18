class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        if node == self.parent[node]:
            return node
        parent = self.find(self.parent[node])
        self.parent[node] = parent
        return parent
        # curr = node
        # while curr != self.parent[curr]:
        #     self.parent[curr] = self.parent[self.parent[curr]]
        #     curr = self.parent[curr]
        # return curr
    
    def union(self, node1, node2):
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
            return True
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += 1
            return True
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
            return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = n
        dsu = DSU(n)
        for parent, node in edges:
            if dsu.union(parent, node):
                result -= 1
        return result

        
        
