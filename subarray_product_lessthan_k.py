def numubarrayproductlessthank(nums,k):
    #thi is the least possible value so we don't have no option  so k<=1
    if k<=1:
        return 0
    left=0
    product=1
    count=0
    for right in range(len(nums)):
        product*=nums[right]
        while product>=k:
            product/=nums[left]
            left+=1
        count+=(right-left+1)
    return count
nums=[10,5,2,6]
print(numubarrayproductlessthank(nums,100))
