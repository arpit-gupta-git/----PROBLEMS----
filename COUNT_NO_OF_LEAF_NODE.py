class Solution:
    def countLeaves(self, root):
        count = 0
        def preorder(root):
            nonlocal count
            if root is None:
                return
            if root.left is None and root.right is None :
                count +=1
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return count 
