# using recursive approach ----------------
def inorder(root):
    if root is None:
        return          # nothing to visit, just stop — no append here
    inorder(root.left)  # go left first
    ans.append(root.val)  # then visit this node
    inorder(root.right) # then go right
