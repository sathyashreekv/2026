def isEven(n):
    rem=n%2
    if rem==0:
        return True
    else:
        return False
def usingBit(n):
    if (n&1)==0:
        return True
    else:
        return False

n=15
print(isEven(n))
print(usingBit(24))
arr=[1,2,3,5]
print(sum(arr))
total_sum=len(arr)*(len(arr)+1)//2
print(total_sum-sum(arr))
    