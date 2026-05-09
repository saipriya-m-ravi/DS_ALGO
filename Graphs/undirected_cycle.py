from collections import defaultdict


class Solution:
    def solve(self, A, B):
        adj=defaultdict(list)
        for i in range(len(B)):
            adj[B[i][0]-1].append(B[i][1]-1) 

        visited = [False]*A
        
        def dfs(u, parent):            
            visited[u]=True
            
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v,u):
                        return True
                elif v != parent:
                    return True

            return False

        for i in range(A):
            if not visited[i] and dfs(i):
                return 1
        return 0
