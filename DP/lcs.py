def lcs_with_string(s1, s2):
    s1 = " " + s1
    s2 = " " + s2
    
    m = len(s1)   # rows
    n = len(s2)   # cols
    
    dp = [[0]*n for _ in range(m)]
    
    # build dp
    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # reconstruct
    i, j = m-1, n-1
    lcs = []
    
    while i > 0 and j > 0:
        if s1[i] == s2[j]:
            lcs.append(s1[i])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return "".join(reversed(lcs))