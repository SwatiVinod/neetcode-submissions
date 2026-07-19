class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)

        result = ['JFK']
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                result.append(v)
                adj[src].pop(i)

                if dfs(v): return True

                result.pop()
                adj[src].insert(i, v)
            return False

        dfs('JFK')
        return result