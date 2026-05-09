from dsu import DSU


class Solution:
    def solve(self, A, B):
        B.sort(key=lambda x:x[2])
        dsu = DSU()
        
        total_cost = 0
        edges = 0
        
        for u,v,w in B:
            if dsu.find(u)!=dsu.find(v):
                dsu.union(u,v)
                total_cost += w
                edges += 1
                if edges == (A-1):
                    break
        
        return total_cost
            