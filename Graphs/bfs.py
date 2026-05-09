from collections import defaultdict, deque


class Solution:
    def solve(self, A, B):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in B:
            graph[u].append(v)

        # BFS to check path from 1 to A
        queue = deque([1])
        visited = set([1])

        while queue:
            u = queue.popleft()
            if u == A:
                return 1

            for v in graph.get(u, []):
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return 0
