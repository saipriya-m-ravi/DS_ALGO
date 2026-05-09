from collections import defaultdict


class Solution:
    def solve(self, A, B):
        adj=defaultdict(list)
        for i in range(len(B)):
            adj[B[i][0]-1].append(B[i][1]-1) 

        visited = [False]*A
        rec_stack = [False] *A
        
        def dfs(u):            
            visited[u]=True
            rec_stack[u]=True
            
            for v in adj[u]:
                if not visited[v]:
                    if dfs(v):
                        return True
                elif rec_stack[v]:
                    return True

            rec_stack[u] = False
            return False 

        for i in range(A):
            if not visited[i] and dfs(i):
                return 1
        return 0
