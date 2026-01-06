# """
# Docstring for containers
# list is an ordered collection ,use when the order matters
# """
# my_list=[0]*4
# for i in range(4):
#     elem=int(input("enter the element"))
#     my_list[i]=elem
# print(my_list)
# """
# If you run that loop with an empty list like my_list = [], 
# your code will crash and throw an IndexError: 
# list assignment index out of range.

# Here is why that happens and how to fix it:

# The Problem
# In Python, an empty list has no slots or "indices."
#  When you try to do my_list[i] = elem, 
#  you are telling Python to go to position i and replace what is there. 
#  Since the list is empty, position 0 doesn't even exist yet, 
#  so Python doesn't know where to put the data.
# """
# """append puhing new element to end of the list"""
# my_bills=[]
# for i in range(4):
#     cost=int(input("enter the cost the item "))
#     my_bills.append(cost)
# print(my_bills)

"""list comprehension =>pythonic ay to create list"""
# my_colors=[input("enter your favourite color ") for i in range(4)]
# print(my_colors)

# fruits=[ input("enter the fruits name :") for i in range(5)]
# print(fruits)

numbers=[1,2,3,4,5,6]
even=[ x for x in numbers if x%2==0]
print(even)
cube=[x**3 for x in numbers if x%2!=0]
print(cube)
""" for conditional if-else 
n=[x if i%2==0 else 0 for _ in range(4)]
"""
n=[x if x%2==0 else 0 for x in range(4)]
print(n)
