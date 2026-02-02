def circular_subarrya_sum(nums):
    total,cur_max,max_res,cur_min,min_res=0,0,nums[0],0,nums[0]

    for n in nums:
        cur_max=max(n,cur_max+n)
        max_res=max(max_res,cur_max)

        cur_min=min(n,cur_min+n)
        min_res=min(min_res,cur_min)

        total+=n
    return max(max_res,total-min_res) if max_res>0 else max_res

