class Solution:
    # @param A : root node
    # @return an integer
    def solve(self, A):

        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 0
            
            if node.val > max_val:
                count = 1
            
            max_val = max(max_val, node.val)
            
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            
            return count
        
        return dfs(A, float('-inf'))