class Solution(object):
	def visit(self, i, j, grid):
		"""
		BFS visit
		"""
		m, n = len(grid), len(grid[0])
		queue = [(i,j)]
		while queue != []:
			(x,y) = queue[0]
			if x != 0 and grid[x-1][y] == "1":
				queue.append((x-1,y))
			if x != m-1 and grid[x+1][y] == "1":
				queue.append((x+1,y))
			if y != 0 and grid[x][y-1] == "1":
				queue.append((x,y-1))
			if y != n-1 and grid[x][y+1] == "1":
				queue.append((x,y+1))
			grid[x][y] = "0"
			# print(str(x) + ',' + str(y))
			queue.pop(0)
		return

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
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(s.numIslands(grid))