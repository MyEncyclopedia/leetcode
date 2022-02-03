# AC
# Runtime: 56 ms, faster than 63.74% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 17.7 MB, less than 73.33% of Python3 online submissions for Kth Smallest Element in a BST.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def ordered_iter(node):
            if node:
                yield from ordered_iter(node.city_a)
                yield node
                yield from ordered_iter(node.city_b)

        for node in ordered_iter(root):
            k -= 1
            if k == 0:
                return node.val