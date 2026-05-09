class Solution:
    def solve(self, A, D, E, F, G, H):
        INF = 10**15

        # distance matrix
        dist = [[INF] * A for _ in range(A)]

        # distance to self
        for i in range(A):
            dist[i][i] = 0

        # roads (bidirectional)
        for u, v, w in zip(D, E, F):
            u -= 1
            v -= 1
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)

        # Floyd–Warshall
        for k in range(A):
            for i in range(A):
                for j in range(A):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # Answer queries
        ans = []
        for u, v in zip(G, H):
            u -= 1
            v -= 1
            ans.append(dist[u][v] if dist[u][v] != INF else -1)

        return ans
