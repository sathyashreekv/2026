def longestSemiRepetitiveSubstring(s):
    max_length=1
    left=0
    pair=0
    window_size=0
    for right in range(1,len(s)):
        if s[right]==s[right-1]:
            pair+=1
        while pair>1:
            if s[left]==s[left+1]:
                pair-=1
            left+=1
        window_size=right-left+1
        max_length=max(max_length,window_size)
    return max_length

s="111101"
print(longestSemiRepetitiveSubstring(s))