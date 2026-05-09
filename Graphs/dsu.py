
# “Union operates on representatives. I always find the roots first, 
# then update parent and size only at the root level.”
# Nodes don’t get merged — roots do.

Amortized TC = O(alpha) = constant (Inverse Ackermann)
SC = O(V)

class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}
        # self.rank = {}
        # self.components = 0
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x]=x
            self.size[x]=1
            # self.rank[x]=0
            # self.components += 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
 ## We want to merge py to px always. So if size of px is smaller than size of py we swap the values.                       
            self.parent[py] = px
            self.size[px] += self.size[py]
            
            # if self.rank[px] < self.rank[py]:
            #     self.parent[px] = py
            # elif self.rank[px] > self.parent[py]:
            #     self.parent[py] = px
            # else:
            #     self.parent[py] = px
            #     self.rank[px] += 1
            
            # self.components -= 1