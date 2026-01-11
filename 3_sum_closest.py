def threesumclosest(nums,target):
    
    nums.sort()
    closest_sum=float('inf')
    for i in range(len(nums)-2):
        
        left=i+1
        right=len(nums)-1
        while left<right:
            current_sum=nums[i]+nums[left]+nums[right]
            if abs(target-current_sum)<abs(target-closest_sum):
                closest_sum=current_sum
            if current_sum<target:
                left+=1
            elif current_sum>target:
                right-=1
            else:
                return target
    return closest_sum

nums=[10,20,30,40,50,60,70,80,90]
print(threesumclosest(nums,1))

    
