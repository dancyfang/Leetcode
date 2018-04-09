# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BST: all left child smaller or equal to root, all right child larger or equal to root
# Use the recursive feature of a tree

# binary search, count number of nodes
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return
        c = self.count(root.left)
        if c > k-1:
            return self.kthSmallest(root.left, k)
        elif c == k-1:
            return root.val
        else:
            return self.kthSmallest(root.right, k-c-1)
        
    def count(self, root):
        if root is None:
            return 0
        else:
            return self.count(root.left) + self.count(root.right) + 1
