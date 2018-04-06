# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def postorder(self, root):
		"""
		caculate the amount of the current subtree rooted by root
		:type root: TreeNode
		:rtype: int, int
		"""
		# y: maximum amount if steal current node
		# n: maximum amount if do not steal current node
		if root is None:
			return 0,0
		ly,ln = self.postorder(root.left)
		ry,rn = self.postorder(root.right)
		y = root.val+ln+rn
		n = max(ly,ln) + max(ry,rn)
		return y,n

	def rob(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		vy,vn = self.postorder(root)
		return max(vy, vn)
        
a = TreeNode(8)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(3)
f = TreeNode(1)
g = TreeNode(8)
h = TreeNode(2)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
d.left = g
d.right = h
s = Solution()
print(s.rob(a))