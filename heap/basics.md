## Binary Heap is a special complete binary tree
Max/Min heap: all parent nodes larger/smaller than children.

Usually implemented using arrays. Index heap elements using 1, 2, .... 

Parent: L[i/2]

Left child: L[2i]

Right child: L[2i+1]

See following picture.


Implementation of basic operations on a min heap
```python
class MinHeap:
    
    def __init__(self):
        self.heap = [None]
        self.size = 0
        
    def parent(self, i):
        return i//2
    
    def leftchild(self, i):
        return 2*i
    
    def rightchild(self, i):
        return 2*i+1
    
    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp
    
    def getMin(self):
        if self.size == 0:
            print('Empty heap!')
            return
        return self.heap[1]
    
    
    def percUp(self, i):
        while self.parent(i) > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)
    
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.percUp(self.size)
    
    def getMinChild(self, i):
        if i > self.parent(self.size):
            print('No children')
        if self.leftchild(i) == self.size or self.heap[self.leftchild(i)] <= self.heap[self.rightchild(i)]:
            return self.heap[self.leftchild(i)], self.leftchild(i)
        return self.heap[self.rightchild(i)], self.rightchild(i)
        
    def percDown(self, i):
        while i <= self.parent(self.size):
            value, index = self.getMinChild(i)
            if value < self.heap[i]:
                self.swap(i, index)
                i = index
            else:
                break
    
    # remove and return min
    def removeMin(self):
        if self.size == 0:
            print('Empty heap!')
            return
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.percDown(1)
        return res
    
    # O(n) time, start from the last parent node, percDown if that parent node is larger than children.
    def buildHeap(self, alist):
        self.__init__()
        self.heap = self.heap + alist[:]
        self.size = len(alist)
        st = self.parent(self.size)
        while st > 0:
            self.percDown(st)
            st -= 1
        
    # O(nlog(n)) time
    def heapSort(self, alist):
        # O(n) time
        self.buildHeap(alist)
        # O(nlog(n)) time
        for i in range(len(alist)-1):
            self.swap(1, self.size)
            self.size -= 1
            self.percDown(1)
        return self.heap[1:][::-1]
        


```



