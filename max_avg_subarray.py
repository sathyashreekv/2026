def  maxavgsubarray(nums,k):
    left=0
    max_average=float('-inf')
    window_sum=0
    for right in range(len(nums)):
        window_sum+=nums[right]
        if right>=k-1:
            max_average=max(max_average,window_sum/k)
            window_sum-=nums[left]
            left+=1
    return max_average

print(maxavgsubarray([1,12,-5,-6,50,3],4))