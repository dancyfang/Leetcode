from collections import defaultdict

class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		# graph is a dictionary of nodes, each node has a list containing adjacent nodes
		self.graph = defaultdict(list)

	def addEdge(self, v, n):
		self.graph[v].append(n)
		self.graph[n].append(v)

	def sortEdge(self):
		for v in self.graph.keys():
			self.graph[v] = sorted(self.graph[v])

	def DFS_utils(self, v, visited):
		visited.append(v);
		print(v);
		for i in self.graph[v]:
			if i not in visited:
				self.DFS_utils(i, visited) # depth first search uses stack, while broad first search uses queue

	def DFS(self, v):
		self.DFS_utils(v, [])
	

A = Graph()
A.addEdge(1,2)
A.addEdge(1,3)
A.addEdge(2,4)
A.addEdge(3,4)
A.addEdge(4,5)
A.addEdge(3,6)
A.addEdge(5,6)
A.sortEdge()
A.DFS(1)
