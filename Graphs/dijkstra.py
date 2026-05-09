import heapq
class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        D=[10**9 for i in range(A)]
        D[C]=0
        min_heap=[]
        
        graph={i:[] for i in range(A)}
        for i in range(len(B)):
            graph[B[i][0]].append((B[i][2],B[i][1]))
            graph[B[i][1]].append((B[i][2],B[i][0]))
        
        for w in graph[C]:
            heapq.heappush(min_heap,w)
        
        while min_heap:
            weight,dest=heapq.heappop(min_heap)
            if D[dest] == 10**9 :
                D[dest]=weight
            
                for w in graph[dest]:
                    if D[w[1]]==10**9:
                        heapq.heappush(min_heap,(w[0]+weight,w[1]))
        
        for i in range(len(D)):
            if D[i]==10**9:
                D[i]=-1
        
        return D