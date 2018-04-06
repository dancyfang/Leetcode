from collections import defaultdict
class Solution(object):	
	def DFS(self, M, i, visited):
		"""
		:type M: List[List[int]]
		:type i: int
		:type visited: list
		:rtype: none
		"""
		visited.append(i)
		# print(i)
		for j in range(len(M)):
			if M[i][j] == 1 and j not in visited:
				self.DFS(M, j, visited)
		return

	def findCircleNum(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		visited = []
		s = 0
		for i in range(len(M)):
			if i in visited:
				continue
			# print('Group ' + str(s))
			self.DFS(M, i, visited)
			s += 1
		return s

# a = Solution()
# M = [[1,1,0],[1,1,1],[0,1,1]]
# print (a.findCircleNum(M))


        