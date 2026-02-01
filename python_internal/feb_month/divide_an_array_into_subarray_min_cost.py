def min_cost(nums):
    n=len(nums)
    first=nums[0]
    min1=float('inf')
    min2=float('inf')

    for i in range(1,n):
        if nums[i]<min1:
            min2=min1
            min1=nums[i]
        elif nums[i]<min2:
            min2=nums[i]
    return first+min1+min2


arr=[1,2,3,12]
print(min_cost(arr))


