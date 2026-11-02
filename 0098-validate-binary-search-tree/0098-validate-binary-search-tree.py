class Solution:
    def isValidBST(self, root):
        def validate(node, minimum, maximum):
            if node is None:
                return True

            if node.val <= minimum or node.val >= maximum:
                return False

            right_valid = validate(node.left, minimum, node.val)
            left_valid = validate(node.right,  node.val, maximum)
            return left_valid and right_valid
        return validate(root, float('-inf'), float('inf'))