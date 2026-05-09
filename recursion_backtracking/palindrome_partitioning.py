def partition(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    
    # Precompute palindrome table
    for end in range(n):
        for start in range(end + 1):
            if s[start] == s[end] and (end - start < 2 or dp[start+1][end-1]):
                dp[start][end] = True
    
    res = []
    
    def backtrack(start, path):
        if start == n:
            res.append(path[:])
            return
        
        for end in range(start, n):
            if dp[start][end]:
                path.append(s[start:end+1])
                backtrack(end+1, path)
                path.pop()
    
    backtrack(0, [])
    return res