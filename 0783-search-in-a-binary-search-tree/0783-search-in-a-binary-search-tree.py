class Solution:
    def searchBST(self, root, target):
        while root and root.val != target:
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return root