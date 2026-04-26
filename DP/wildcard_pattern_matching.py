def isMatch_wildcard(s, p):
    s = " " + s
    p = " " + p
    
    n = len(s)
    m = len(p)
    
    dp = [[False] * (n) for _ in range(m)]
    
    dp[0][0] = True
    
    # pattern vs empty string
    for i in range(1, m):
        if p[i] == '*':
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, m):      # pattern
        for j in range(1, n):  # string
            
            # match one char
            if p[i] == s[j] or p[i] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            
            # '*' matches anything
            elif p[i] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]