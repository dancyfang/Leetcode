class Solution:
    # construct a heap using the first row, each time: retrieve the heap top,
    # and replace it with the number below it in the same column.
    # Merge n sorted arrays + heap remove top, O(Klog(n)) time
    def getMinChild(self, i, heap):
        sz = len(heap) - 1
        if i > sz//2:
            print('No child')
            return
        if 2*i == sz or heap[2*i][2] < heap[2*i+1][2]:
            return 2*i
        return 2*i+1
        
    def percDown(self, i, heap):
        sz = len(heap) - 1
        while i <= sz//2:
            ind = self.getMinChild(i, heap)
#             print(heap[i], heap[ind])
            if heap[i][2] > heap[ind][2]:
                temp = heap[i]
                heap[i] = heap[ind]
                heap[ind] = temp
                i = ind
            else:
                break
        
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = [None] + [(0,i,v) for i,v in enumerate(matrix[0])]
#         print(heap)
        for i in range(k):
#             print(i)
            top = heap[1]
#             print(top)
            if top[0] < len(matrix) - 1:
                heap[1] = (top[0]+1, top[1], matrix[top[0]+1][top[1]])           //?????????
                self.percDown(1, heap)
            else:
                heap[1] = heap[-1]
                heap.pop()
                self.percDown(1, heap)
#             print(heap)
        return top[2]
