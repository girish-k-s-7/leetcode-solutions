class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # Check whether we reached a leaf
        if root.left is None and root.right is None:
            return root.val == targetSum

        remaining = targetSum - root.val

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )