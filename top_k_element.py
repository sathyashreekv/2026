"""
Find the top k elements in a list

1 approach use the freq then sorted then by their frequency pick the top k element then return them
2 approach use heapq to find the top k elements based on their frequency
3 use bucket sort to group elemnts by their frequency and then pick the top k elements
in bucket sort we store index as fequency and at value we store the list of elemnents with that frequency then we iterate from from highest  to lowest frequency and pick the top k elements =>0(n) time complexity

"""

def top_k_elements(nums,k):
    count={}
    for num in nums:
        count[num]=count.get(num,0)+1
    freq=[[] for _ in range(len(nums)+1)]
    for num,frequency in count.items():
        freq[frequency].append(num)
    res=[]
    for i in range(len(freq)-1,0,-1):
        for i in freq[i]:
            res.append(i)
            if len(res)==k:
                return res
            
nums=[1,1,1,2,2,3,3,4,5,5,5,5]
k=4
print(top_k_elements(nums,k))


