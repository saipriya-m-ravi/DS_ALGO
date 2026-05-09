def solve(A):
    n = len(A)
    prev_greater = [-1]*n
    next_greater = [n]*n
    st = []
    
    for i in range(n):
        while st and A[st[-1]] <= A[i]:
            st.pop()    
        if st:
            prev_greater[i] = st[-1]
        st.append(i)
    
    st.clear()
    
    for i in range(n-1, -1, -1):
        while st and A[st[-1]] < A[i]:
            st.pop()
        
        if st:
            next_greater[i] = st[-1]
        st.append(i)
        
    