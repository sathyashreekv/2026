def maxsum(arr,n,k):
    max_sum=float('-inf')
    for i in range(n-k+1):
        current_sum=0
        for j in range(k):
            current_sum+=arr[i+j]
        max_sum=max(max_sum,current_sum)
    return max_sum

def fixed_window_sum(arr,n,k):
    if n<=k:
        return -1
    max_sum=float('-inf')
    left=0
    for right in range(n):
        window_sum+=arr[right]
        if right-left+1==k:
            max_sum=max(max_sum,window_sum)
            window_sum-=arr[left]
            left+=1
    return max_sum

arr=[-1,2,3,4,5]
print(maxsum(arr,len(arr),3))
print(fixed_window_sum(arr,len(arr),3))
"""sliding window approch"""