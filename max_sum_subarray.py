def maxsum(arr,k):
    max_sum=0
    window_sum=0
    left=0
    for right in range(len(arr)):
        window_sum+=arr[right]
        if right>=k-1:

            if window_sum>max_sum:
                max_sum=window_sum
            window_sum-=arr[left]
            left+=1
    return max_sum

arr=[2,1,5,1,3,2]
k=3
print(maxsum(arr,k))