def numberOfSubstrings(s):
    n=len(s)
    res=0
    left=0
    count={
        'a':0,
        'b':0,
        'c':0
    }
    for right in range(n):
        count[s[right]]+=1
        while count['a']>0 and count['b']>0 and count['c']>0:
            count[s[left]]-=1
            left+=1
        res+=left
    return res

s="abcabc"
print(numberOfSubstrings(s))