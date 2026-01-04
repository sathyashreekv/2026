def findconsecutive(nums):
    current=0
    maximum=0
    for num in nums:
        if num==1:
            current+=1
        else:
            current=0
        maximum=max(maximum,current)
    return maximum
print(findconsecutive([1,1,0,1,1,1]))