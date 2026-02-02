"""
Docstring for python_internal.feb_month.kadane_algo.largest_sum

In this quetion we are going to find a non-empty subarray with larget sum
from a given array of integers using Kadane's Algorithm.

Brute force approach would be to consider all the subarray and calculate the sum
and return the maximum sum. This approach would take O(n^2) time.

"""
def brute_force(nums):
    max_sum=nums[0]
    for i in range(len(nums)):
        cursum=0
        for j in range(i,len(nums)):

            cursum+=nums[j]
            max_sum=max(max_sum,cursum)
        return max_sum
def kadane_algorithm(nums):
    max_sum=float('-inf')
    cursum=0
    for n in nums:
        cursum=max(cursum,0)
        cursum+=n
        max_sum=max(max_sum,cursum)
    return max_sum



arr=[4,-1,2,-7,3,4]
print(brute_force(arr))
print(kadane_algorithm(arr))