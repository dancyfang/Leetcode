## Binary Heap is a special complete binary tree
Max/Min heap: all parent nodes larger/smaller than children.

Usually implemented using arrays. Index heap elements using 0, 1, 2, .... 

Parent: L[(i-1)/2]

Left child: L[2i+1]

Right child: L[2i+2]

See following picture.


Implementation of basic operations on a min heap
```python
class MinHeap:
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
        self.heap[j] = self.heap[i]
        self.heap[i] = temp
    
    def getMin(self):
        return self.heap[1]
    
    
    def percUp(self, i):
        while self.parent(i) > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)
    
    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.percUp(self.size)
    
    def percDown(self, i):
        while self.leftchild(i) < self.size and self.heap[i] > min(self.heap[self.leftchild(i)], self.heap[self.rightchild(i)]):
            if self.heap[self.leftchild(i)] < self.heap[self.rightchild(i)]:
                self.swap(i, self.leftchild(i))
                i = self.leftchild(i)
            else:
                self.swap(i, self.rightchild(i))
                i = self.rightchild(i)            
    
    # remove and return min
    def removeMin(self):
        res = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.percDown(1)
        return res
    
    # O(n)
    def buildheap(self, alist):


```



