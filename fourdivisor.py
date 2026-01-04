def findfourdivisor(nums):
    total=0
    for num in nums:
        sum=0
        count=0
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                if i*i==num:
                    sum+=i
                    count+=1
                else:
                    sum+=(i+num//i)
                    count+=2
            if count>4:
                break
        if count==4:
            total+=sum
    return total

nums=[21,21]
print(findfourdivisor(nums))
"""
Dry run
[21,21]
i=0 =>21 (sqrt(21) approx=4)=>[1,21,3,7](1*21,21*1,3*7,7*3) count=4 sum=1+21+3+7=>32
i=1 =>21 same 32
total=>32+32=>64

"""