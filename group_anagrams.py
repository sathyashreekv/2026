"""
Docstring for group_anagrams

grouping anagrams means to categories words with same letters together then returning their list of values
we can use hashmap to store the sorted version of the word as key and the list of words as values then return the values of the  hashmap as list of lists 

"""
def group_anagrams(strs):
    freq={}
    for word in strs:
        sorted_word=''.join(sorted(word))
        if sorted_word not in freq:
            freq[sorted_word]=[]
        freq[sorted_word].append(word)
    return list(freq.values())


strs=['eat','ten','ent','net','bat','tab','tea','ate','atb']
print(group_anagrams(strs))