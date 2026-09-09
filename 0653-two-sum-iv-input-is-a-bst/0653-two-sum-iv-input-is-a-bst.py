class Solution:
    def findTarget(self, root, k):
        arr = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        inorder(root)
        left = 0
        right = len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        return False