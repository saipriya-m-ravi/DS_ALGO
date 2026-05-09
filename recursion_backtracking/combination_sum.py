import sys
sys.setrecursionlimit(10**9)


def combinationSum(candidates, target):
    res = []
    candidates = list(set(sorted(candidates)))

    def backtrack(start, remaining, path):
        if remaining == 0:
            res.append(path[:])
            return
        
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Choose current element
            path.append(candidates[i])
            
            # Stay at i (because unlimited reuse)
            backtrack(i, remaining - candidates[i], path)
            
            # Undo choice
            path.pop()

    backtrack(0, target, [])
    return res

print(combinationSum([0,1,2,3,4],3))
