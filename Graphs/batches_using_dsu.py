from dsu import DSU


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        dsu = DSU()
        for u,v in C:
            dsu.union(u,v)
        
        strength = {}
        for i in range(1, A+1):
            pi = dsu.find(i)
            strength[pi] = strength.get(pi, 0)+B[i-1]
        
        count=0
        for v in strength.values():
            if v>=D:
                count+=1
        return count