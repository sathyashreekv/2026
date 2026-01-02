"""
Docstring for python_internal.understanding_data
In python every piece of data is stored/enscapsulated as an Pyobject
each pyobject has 3 attributes 
1 identity ->id() function gives the memory address of the object (immutable)
2 type ->type() function helps to know the type of object and wt operation we can perform on it (immutable)
3 value -> the actual data stored in the object
value chnaged->mutable object such as list ,dictionary
value not changed -> immutable objects (string,numbers,tuples)

"""

x=10
print(id(x))
print(type(x))

x=x+5
print(id(x))
my_list=[1,2]
print(id(my_list))
print(type(my_list))
my_list.append(3)
print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_list[2]))
my_tuple=(1,my_list)
print(id(my_tuple))
print(type(my_tuple))
print(my_tuple[1])
print(id(my_tuple[0]))
print(id(my_list))

a=1
b=1
print(id(a))
print(id(b))

c=d=[]
print(id(c))
print(id(d))
c=[]
d=[]
print(id(c))
print(id(d))
a = 257
b = 257 
print(a is b) 
""" here is is boolean operator which checks the identity of the object 
it returns true if both the operands point to the same object
"""
a=257
b=257
print(id(a))
print(id(b))
print(a is b)
""" You read that Objects are never explicitly destroyed; they are collected when unreachable. In CPython, this happens via Reference Counting."""
import sys
x=[1,2,3]
print(sys.getrefcount(x))
y=x
print(sys.getrefcount(x))