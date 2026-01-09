def threesumclosest(nums,target):
    
    nums.sort()
    for i in range(len(nums)-2):
        closest_sum=nums[i]+nums[i+1]+nums[i+2]
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

nums=[-1, -1, 0, 1, 1]
print(threesumclosest(nums,0))

    
