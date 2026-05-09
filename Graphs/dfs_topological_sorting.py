from collections import defaultdict


class Solution:
    def solve(self, A, B):
        adj = defaultdict(list)
        for u, v in B:
            adj[u].append(v)
        
        visited = [False] * (A+1)
        rec_stack = [False] * (A+1)
        stack = []
        self.hascycle = False
        
        def dfs(u):
            visited[u] = True
            rec_stack[u] = True
            
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
                elif rec_stack[v]:
                    self.hascycle = True
            
            rec_stack[u] = False
            stack.append(u)
        
        for i in range(1, A + 1):
            if not visited[i]:
                dfs(i)

        if self.has_cycle:
            return []

        return stack[::-1]