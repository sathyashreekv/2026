def containsNearbyDupliacte(nums,k):

    window_size=set()
    left=0
    for right in range(len(nums)):
        if right>k:
            window_size.remove(nums[left])
            left+=1
        if nums[right] in window_size:
            return True
        window_size.add(nums[right])
    return False

print(containsNearbyDupliacte([1,2,3,1],3))