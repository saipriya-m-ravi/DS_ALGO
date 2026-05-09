from collections import deque

def slidingMaximum(A, B):
    n = len(A)

    if B > n:
        return [max(A)]

    dq = deque()
    ans = []

    for i in range(n):
        # Remove elements outside window
        if dq and dq[0] <= i - B:
            dq.popleft()

        # Remove smaller elements
        while dq and A[dq[-1]] <= A[i]:
            dq.pop()

        dq.append(i)

        # Window formed
        if i >= B - 1:
            ans.append(A[dq[0]])

    return ans
