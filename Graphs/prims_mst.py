from collections import defaultdict
import heapq


class Solution:
    def solve(self, A, B):
        adj_list = defaultdict(list)
        for u,v,w in B:
            adj_list[u].append((w,v))
            adj_list[v].append((w,u))
        
        min_heap = [(0,1)]
        visited = set()
        total_cost = 0
        
        while min_heap:
            cost,node = heapq.heappop(min_heap)
            if node in visited:
                continue
            
            visited.add(node)
            total_cost += cost
            for x in adj_list[node]:
                if x[1] not in visited:
                    heapq.heappush(min_heap, x)
        return total_cost