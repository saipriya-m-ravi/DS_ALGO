def evaluate(S):
    sign_st = [1]
    current_sign = 1
    result = [0]*26
    
    for ch in S:
        if ch == '+':
            current_sign = sign_st[-1]
        elif ch == '-':
            current_sign = -1 * sign_st[-1]
        elif ch == '(':
            sign_st.append(current_sign)
        elif ch == ')':
            sign_st.pop()
        else:
            idx = ord(ch) - ord('a')
            result[idx] = current_sign
    return result


def solve(A, B):
    return 1 if evaluate(A) == evaluate(B) else 0


A = "-(a+b+c)"
B = "-a-b+c"
print(solve(A, B))


# Push when entering (
# Pop when leaving )
# “Everything inside follows curr_sign”
# “What sign applies to everything inside these brackets?”
