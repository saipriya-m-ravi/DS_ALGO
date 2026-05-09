from collections import defaultdict, deque

class Solution:
    def solve(self, A, B):
        adj = defaultdict(list)
        for u, v in B:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * A  # -1 = uncolored, 0 & 1 are two colors

        for start in range(A):
            if color[start] != -1:
                continue

            queue = deque([start])
            color[start] = 0

            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return 0  # not bipartite

        return 1
