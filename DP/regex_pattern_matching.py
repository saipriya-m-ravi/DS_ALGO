def isMatch_regex(s, p):
    s = " " + s
    p = " " + p
    
    n = len(s)   # string length
    m = len(p)   # pattern length
    
    # dp[i][j] → pattern[1..i] vs string[1..j]
    dp = [[False] * (n) for _ in range(m)]
    
    dp[0][0] = True
    
    # pattern vs empty string
    for i in range(2, m):
        if p[i] == '*':
            dp[i][0] = dp[i - 2][0]
    
    for i in range(1, m):      # pattern
        for j in range(1, n):  # string
            
            # Case 1: normal char or '.'
            if p[i] == s[j] or p[i] == '.':
                dp[i][j] = dp[i - 1][j - 1]
            
            # Case 2: '*'
            elif p[i] == '*':
                
                # zero occurrence of previous char
                dp[i][j] = dp[i - 2][j]
                
                # one or more occurrence
                if p[i - 1] == s[j] or p[i - 1] == '.':
                    dp[i][j] |= dp[i][j - 1]
    
    return dp[m][n]
