class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        A = list(map(int, A))
        
        flipped = [0]*n
        active = 0
        ans = 0
        
        for i in range(n):
            
            # remove expired flip
            if i >= B:
                active ^= flipped[i-B]
            
            # effective bit after flips
            if A[i] ^ active == 0:
                
                # can't flip if not enough space
                if i + B > n:
                    return -1
                
                flipped[i] = 1
                active ^= 1
                ans += 1
        
        return ans