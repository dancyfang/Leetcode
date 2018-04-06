class Solution(object):
	def visit(self, i, j, grid):
		m, n = len(grid), len(grid[0])
		if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
			return
		# print(str(i) + ',' + str(j))
		grid[i][j] = "0"
		self.visit(i-1,j,grid)
		self.visit(i+1,j,grid)
		self.visit(i,j-1,grid)
		self.visit(i,j+1,grid)

	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if not grid:
			return 0
		count = 0
		m, n = len(grid), len(grid[0])
		for i in range(m):
			for j in range(n):
				if grid[i][j] == "1":
					count += 1
					# print('count:',count)
					self.visit(i, j, grid)
		return count

s = Solution()
# grid = []
grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
print(s.numIslands(grid))