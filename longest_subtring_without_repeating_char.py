"""
Docstring for longest_subtring_without_repeating_char
longest ->means max length keepin mind for this question the idea is keep track of length update it when required 
and memory (for checking whether a particular char is already present in the memory if present remove the elemnt until the right not in memory 
using left pointer for every add update the max length)
"""
def longestSubstring(s):
    left=0
    max_length=0
    memory=set()
    for right in range(len(s)):
        #found duplicate?
        while s[right] in memory:
            memory.remove(s[left])
            left+=1
       #without duplicate valuess
        if s[right] not in memory:
            memory.add(s[right])
            max_length=max(max_length,right-left+1)
    return max_length,memory

print(longestSubstring("pwwkew"))
print(longestSubstring("abcabcbb"))
