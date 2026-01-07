"""
Docstring for reverse
Reverse uing 2 pointer approach

s= |h|e|l|l|o|
s=|o|l|l|e|h|

"""
def reverse_str(s):
    char_list=list(s)
    left=0
    right=len(s)-1
    while left<right:
        char_list[left],char_list[right]=char_list[right],char_list[left]
        left+=1
        right-=1
    
    return " ".join(char_list)
s="happy"
print(reverse_str(s))
"""
crashes string ued because string i immutable so need to convert to list then use
"""