def lowestCommonAncestor(root, p, q):
    
    if not root:
        return None
    
    if root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    
    return left if left else right

##########################################BST############################################

def lowestCommonAncestor(root, p, q):

    while root:
        
        if p.val < root.val and q.val < root.val:
            root = root.left
        
        elif p.val > root.val and q.val > root.val:
            root = root.right
        
        else:
            return root