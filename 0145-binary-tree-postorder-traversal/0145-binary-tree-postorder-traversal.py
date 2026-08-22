class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        postorder = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            postorder.append(node.val)
        return postorder