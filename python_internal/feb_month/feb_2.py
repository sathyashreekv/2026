import heapq
m=k-1
left_heap=[]
right_heap=[]
to_remove={}
current_sum=0

def clean(heap,is_max_heap):
    while heap:
        val=-heap[0]  if is_max_heap else heap[0]
        if to_remove.get(val,0)>0:
            heapq.heappop(heap)
            to_remove[val]-=1
        else:
            break
    