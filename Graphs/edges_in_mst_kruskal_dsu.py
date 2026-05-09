class Solution:
    def solve(self, A, B):
        ans = [0 for _ in range(len(B))]
        parent = {}
        rank ={}
        edges = [(B[i][2], B[i][0], B[i][1], i) for i in range(len(B))]
        edges.sort()

        def find(x):
            if x not in parent:
                parent[x]=x
                rank[x]=0
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y):
            px,py = find(x),find(y)
            if px==py:
                return False
            
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[px]>rank[py]:
                parent[py]=px
            else:
                parent[py]=px
                rank[px] += 1
            return True
        
        i=0
        while i<len(edges):
            j=i
            while j<len(edges) and  edges[i][0]==edges[j][0]:
                j+=1
            
            for k in range(i,j):
                if find(edges[k][1])!=find(edges[k][2]):
                    ans[edges[k][3]]=1
            
            for k in range(i,j):
                union(edges[k][1],edges[k][2])

            i=j
        return ans