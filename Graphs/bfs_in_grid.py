from collections import deque


class Solution:
    def solve(self, A, B, C, D, E, F):
        grid = [[1] * (B+1) for _ in range(A+1)]

        for i in range(A+1):
            for j in range(B+1):
                for k in range(C):
                    dist = ((E[k]-i)**2 + (F[k]-j)**2)
                    if dist <= D**2:
                        grid[i][j] = 0
                        break
                      
        if not grid[0][0] or not grid[A][B]:
            return "NO"

        queue = deque([(0,0)])
        grid[0][0] = -1
        directions = [(0,1),(1,0),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]

        while queue:
            x,y = queue.popleft()
            if x==A and y==B:
                return "YES"
            for dx,dy in directions:
                newx,newy = x+dx, y+dy
                if 0<=newx<=A and 0<=newy<=B and grid[newx][newy]==1:
                    queue.append((newx,newy))
                    grid[newx][newy] = -1
        
        return "NO"
