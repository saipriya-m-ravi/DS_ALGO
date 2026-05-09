import heapq

class Solution:
    def solve(self, A, B):
        inv = sorted(zip(A,B))
        minheap = []

        for expiry, profit in inv:
            heapq.heappush(minheap, profit)
            if len(minheap) > expiry:
                heapq.heappop(minheap)
        
        return sum(minheap) % (pow(10, 9)+7)
