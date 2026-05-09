class Solution:
    def solve(self, grid):
        if not grid:
            return 0
     
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
      
        def dfs(i, j):
            if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]==0:
                return
            
            grid[i][j] = 0
            for dx, dy in directions:
                dfs(i+dx, j+dy)
        
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    islands += 1
                    dfs(row, col)
        return islands