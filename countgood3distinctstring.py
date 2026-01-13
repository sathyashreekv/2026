def countgoodstring(s):
    count=0
    for i in range(len(s)-2): #at last 2 elements wt to do our window size is 3 soo stopping here
        window=s[i:i+3]
        if len(set(window))==3:#checking if they are unique
            count+=1 #tracking the good strings
            print(window)
    return count


s="xzyyzaz"
print(countgoodstring(s))