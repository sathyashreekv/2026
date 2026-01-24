
def missing_number(nums):
    xor_all=0
    for i in range(0,len(nums)):
        xor_all^=nums[i] 
    return xor_all
nums=[1,1,2,2,3,3,4,4,5]
print(missing_number(nums))
