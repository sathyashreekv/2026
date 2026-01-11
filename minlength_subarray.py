def minlength(nums,target):
    min_length=float('inf')
    window_sum=0
    left=0
    for right in range(len(nums)):
        window_sum+=nums[right]
        while window_sum>=target:
            min_length=min(min_length,right-left+1)
            window_sum-=nums[left]
            left+=1
    return 0 if min_length == float('inf') else min_length


nums=[10,20,30,40,50,60,70,80,90]
print(minlength(nums,100))
