"""
Docstring for practice_heap
Building min heap fom scratch 
as we know min heap ->root ->index 0 ha smallest element compared to its children

"""
class MinHeap:
    def __init__(self):
        self.heap=[]
    def push(self,val):
        self.heap.append(val)
        self._sift_up(len(self.heap)-1)
    def _sift_up(self,i):
        parent=(i-1)//2
        if i>0 and self.heap[i]<self.heap[parent]:
            self.heap[i],self.heap[parent]=self.heap[parent],self.heap[i]
            self._sift_up(parent)
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._sift_down(0)
        return root
    def _sift_down(self,i):
        smallest=i
        left=2*i+1
        right=2*i+2
        if left<len(self.heap) and self.heap[left]<self.heap[smallest]:
            smallest=left
        if right<len(self.heap) and self.heap[right]<self.heap[smallest]:
            smallest=right
        if smallest!=i:
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            self._sift_down(smallest)
    def build_heap(self):
        n=len(self.heap)
        start_index=(n//2)-1
        for i in range(start_index,-1,-1):
            self._sift_down(i)
    



h=MinHeap()
h.push(5)
h.push(20)
h.push(15)
h.push(2)

print(h.pop())
print(h.pop())