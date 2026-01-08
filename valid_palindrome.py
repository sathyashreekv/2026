def checkPalindrome(s):
    
    s=s.lower()
    for char in s:
        if not char.isalnum():
            s=s.replace(char,"")
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

s=" "
print(checkPalindrome(s))