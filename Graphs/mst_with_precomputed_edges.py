class Solution:
    def solve(self, A):
        n = len(A)

        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]
            return True

        # Step 1: Pre-connect towns with distance = 1
        for i in range(n):
            for j in range(i + 1, n):
                dx = A[i][0] - A[j][0]
                dy = A[i][1] - A[j][1]
                if dx * dx + dy * dy == 1:
                    union(i, j)

        # Step 2: Build all candidate edges
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                dx = A[i][0] - A[j][0]
                dy = A[i][1] - A[j][1]
                cost = dx * dx + dy * dy
                edges.append((cost, i, j))

        # Step 3: Kruskal
        edges.sort()
        total_cost = 0

        for cost, u, v in edges:
            if union(u, v):
                total_cost += cost

        return total_cost
