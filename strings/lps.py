def build_lps(s):
    lps=[0]*len(s)
    j=0

    for i in range(1,len(s)):
        while j>0 and s[i]!=s[j]:
            j=lps[j-1]

        if s[i]==s[j]:
            j+=1
            lps[i]=j

    return lps