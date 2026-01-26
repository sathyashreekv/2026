"""
Docstring for valid_anangram
anangram is a different words with same letters and same length 
for checking anagram as valid first we compare both words length then we sort both words nad comapre if both are same then they are anagrams

"""
def valid_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq={}
    for char in s1:
        freq[char]=freq.get(char,0)+1
    
    for char in s2:
        if char not in freq or freq[char]==0:
            return False
        freq[char]-=1
    return True
s1='nagrama'
s2='anagram'
print(valid_anagram(s1,s2))


