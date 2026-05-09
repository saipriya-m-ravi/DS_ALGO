def palindromePairs(words):
    def isPal(s):
        return s == s[::-1]
    
    index = {w:i for i,w in enumerate(words)}
    res = []
    
    for i, word in enumerate(words):
        for cut in range(len(word)+1):
            
            prefix = word[:cut]
            suffix = word[cut:]
            
            # Case 1: prefix palindrome
            # look for reverse(suffix) before word
            if isPal(prefix):
                rev = suffix[::-1]
                if rev in index and index[rev] != i:
                    res.append([index[rev], i])
            
            # Case 2: suffix palindrome
            # look for reverse(prefix) after word
            # cut != len(word) prevents duplicates
            if cut != len(word) and isPal(suffix):
                rev = prefix[::-1]
                if rev in index and index[rev] != i:
                    res.append([i, index[rev]])
    
    return res