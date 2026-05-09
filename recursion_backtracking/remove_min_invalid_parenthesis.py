class Solution:
    def solve(self, s):
        
        # Step 1: count extra parentheses
        left_remove = right_remove = 0
        
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove == 0:
                    right_remove += 1
                else:
                    left_remove -= 1
        
        res = set()
        
        def backtrack(index, left_count, right_count, left_remove, right_remove, path):
            
            if index == len(s):
                if left_remove == 0 and right_remove == 0:
                    res.add(path)
                return
            
            ch = s[index]
            
            # Option 1: Remove this parenthesis
            if ch == '(' and left_remove > 0:
                backtrack(index+1, left_count, right_count,
                          left_remove-1, right_remove, path)
            
            elif ch == ')' and right_remove > 0:
                backtrack(index+1, left_count, right_count,
                          left_remove, right_remove-1, path)
            
            # Option 2: Keep it
            if ch not in '()':
                backtrack(index+1, left_count, right_count,
                          left_remove, right_remove, path + ch)
            
            elif ch == '(':
                backtrack(index+1, left_count+1, right_count,
                          left_remove, right_remove, path + ch)
            
            elif ch == ')' and left_count > right_count:
                backtrack(index+1, left_count, right_count+1,
                          left_remove, right_remove, path + ch)
        
        backtrack(0, 0, 0, left_remove, right_remove, "")
        
        return list(res)