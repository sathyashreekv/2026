def avgofsubarray(arr,k):
    result=[]
    current_sum=0
    left=0
    for right in range(len(arr)):
        current_sum+=arr[right]
        if right>=k-1:
            result.append(current_sum/k)
            current_sum-=arr[left]
            left+=1
    return result

arr=[1,3,2,6,-1]
k=3
print(avgofsubarray(arr,k))