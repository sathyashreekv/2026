def findSum(arr):
    arr.sort()
    result=[]
    for i in range(len(arr)):
        if i>0 and  arr[i]==arr[i-1]:
            continue
        left=i+1
        right=len(arr)-1
        target=-arr[i]
        while left<right:
            if arr[left]+arr[right]==target:
                result.append([arr[i],arr[left],arr[right]])
                left+=1
                right-=1

                while left<right and arr[left]==arr[left-1]:
                    left+=1
                while left<right and arr[right]==arr[right+1]:
                   right-=1
            if arr[left]+arr[right]<target:
                left+=1
            if arr[left]+arr[right]>target:
                right-=1
    return result



arr=[-1,0,1,2,-1,-4]
print(findSum(arr))


