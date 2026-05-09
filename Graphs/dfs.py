from collections import defaultdict


class Solution:
    def solve(self, A, B):
        graph = defaultdict(list)
        for u, v in B:
            graph[u].append(v)

        visited = set()

        def dfs(u):
            if u == A:
                return True
            visited.add(u)
            for v in graph.get(u, []):
                if v not in visited and dfs(v):
                    return True
            return False

        return 1 if dfs(1) else 0
