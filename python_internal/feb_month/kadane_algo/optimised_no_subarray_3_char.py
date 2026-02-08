def numberofSubarray(s):
    last_pos={
        'a':-1,
        'b':-1,
        'c':-1
    }
    count=0
    for i in range(len(s)):
        last_pos[s[i]]=i
        shortest_start=min(last_pos['a'],last_pos['b'],last_pos['c'])
        if shortest_start!=-1:
            count+=shortest_start+1
    return count

print(numberofSubarray("abcabc"))