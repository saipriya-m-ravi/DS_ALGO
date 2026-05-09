def generate_parenthesis(N):
    res = []
    
    def backtrack(curr, open_count, closed_count):
        if len(curr) == 2*N:
            res.append(curr)
            return
        
        if open_count < N:
            backtrack(curr+"(", open_count+1, closed_count)
        
        if closed_count < open_count:
            backtrack(curr+")", open_count, closed_count+1)        
    
    backtrack("", 0, 0)
    return res


print(generate_parenthesis(3))
