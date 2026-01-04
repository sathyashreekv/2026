def finderrornum(nums):
    """"
    this is mathematical way
    """
    n=len(nums)
    expected_value=n*(n+1)//2
    actual_value=sum(nums)
    unique_value=sum(set(nums))
    missing=expected_value-unique_value
    duplicate=actual_value-unique_value
    return [duplicate,missing]
def findway2(nums):
    duplicate=-1
    missing=-1
    for val in nums:
        index=abs(val)-1

        if nums[index]<0:
            duplicate=abs(val)
        else:
            nums[index]*=-1
    for i in range(len(nums)):
        if nums[i]>0:
            missing=i+1
    return [duplicate,missing]



nums=[1,2,3,3,5]
print(finderrornum(nums))
print(findway2(nums))