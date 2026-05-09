class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
            
    # map value -> inorder index
        inorder_map = {val: i for i, val in enumerate(A)}       
        post_idx = len(B)-1
        
        def helper(left, right):
            nonlocal post_idx        
            
            if left > right:
                return None
            
            # root from postorder
            root_val = B[post_idx]
            root = TreeNode(root_val)
            post_idx -= 1
            
            # find root index in inorder
            idx = inorder_map[root_val]
            
            # IMPORTANT: build right first
            root.right = helper(idx + 1, right)
            root.left = helper(left, idx - 1)
            
            return root
        
        return helper(0, len(A) - 1)