def shuffle_way(nums,n):
    for i in range(n):
        nums[i]=nums[i]+(nums[i+n]*1024) #encoding pass =>(storing both values in one becuae of 32 bit we use 20 bits )
    for i in range(n-1,-1,-1):#decoding these into even and odd  index x->even and y=>odd
        val=nums[i]
        x=val%1024
        y=val//1024
        nums[2*i]=x
        nums[2*i+1]=y
    return nums
print(shuffle_way([2,5,1,3,4,7],3))
