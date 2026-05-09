class Solution:
    def solve(self, A):
        n, m = len(A), len(A[0])
        count = 0

        for i in range(n):
            for j in range(m): 
                if  A[i][j] == 1: 
                    u, v = i, j
                if A[i][j] == 2:
                    x, y = i, j
                if A[i][j] != -1:
                    count += 1
                    
        direc = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(u, v, visited, free_cell):
            if u==x and v==y:
                return 1 if free_cell==0 else 0
            
            paths = 0
            visited.add((u,v))
            for d in direc:
                new_u = u + d[0]
                new_v = v + d[1]
                if 0 <= new_u < n and 0 <= new_v < m and (new_u, new_v) not in visited and A[new_u][new_v] != -1:
                    paths += dfs(new_u, new_v, visited, free_cell-1)
                
            visited.remove((u, v))
            return paths

        return dfs(u, v, set(), count-1)

        