import heapq
from collections import defaultdict


class Solution:
    def solve(self, A, B):
        adj = defaultdict(list)
        indegree = {i:0 for i in range(1,A+1)}
        for u, v in B:
            adj[u].append(v)
            indegree[v] += 1
        
        topo = []
        minheap = []
        for k,v in indegree.items():
            if v==0:
                heapq.heappush(minheap, k)
        
        while minheap:
            node = heapq.heappop(minheap)
            topo.append(node)
            
            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    heapq.heappush(minheap, v)
        
        if len(topo) < A:
            return []
        return topo
