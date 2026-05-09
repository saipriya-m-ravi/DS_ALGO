class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):

        def height(node):
            if not node:
                return 0
            
            left = height(node.left)
            if left == -1:
                return -1
            
            right = height(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return 0 if height(A) == -1 else 1