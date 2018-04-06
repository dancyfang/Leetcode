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

	def BFS(self, v):
		visited = [v]
		queue = [v]
		print('Adding ' + str(v))
		while queue != []:
			head = queue[0]
			for i in self.graph[head]:
				if i not in visited:
					visited.append(i)
					queue.append(i)
					print('Adding ' + str(i))
			print('Removing ' + str(queue.pop(0)))	

A = Graph()
A.addEdge(1,2)
A.addEdge(1,3)
A.addEdge(2,4)
A.addEdge(3,4)
A.addEdge(4,5)
A.addEdge(3,6)
A.addEdge(5,6)
A.sortEdge()
A.BFS(1)
