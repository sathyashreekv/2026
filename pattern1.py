"""
Docstring for pattern1
List 
Two pointer pattern =>shrinking window by moving to pointers(variables) fom both the end(left) and (right) untl they meet

needed: moving pointer loop

interview =>brute,better,best (optimal)

"""
def bruteum(num,target):
    for i in range(len(num)):
        for j in range(1,len(num)-1):
            if num[i]+num[j]==target:
                return [i,j]
"""
Brute is very slow for large set of num=10^4 numbers then we need to itertes check or operate =>10^4*10^4  operations (comparion)

"""
       
def twosum(num,target):
    left=0
    right=len(num)-1
    while left<right:
        current_sum=num[left]+num[right]
        if current_sum==target:
            return [left,right]
        elif current_sum<target:
            left+=1
        else:
            right-=1


my_bills=[10,20,30,40,50]
bound=50
print(twosum(my_bills,bound))
left=0
right=len(my_bills)-1
while left < right:
    print(f"the left value {my_bills[left]} and the right value {my_bills[right]}")
    left+=1
    right-=1


