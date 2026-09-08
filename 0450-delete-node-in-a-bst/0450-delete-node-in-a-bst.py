class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            curr = root.right

            while curr.left:
                curr = curr.left
            root.val = curr.val

            root.right = self.deleteNode(root.right, curr.val)
        return root