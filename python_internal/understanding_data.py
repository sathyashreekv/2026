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
"""
refrence count =>x =2 then y=x =>then it is 3
underhood:

When you ran sys.getrefcount(x), you likely saw a number higher than you expected. Here is why:

Count = 1: When you created the object x = [1, 2, 3], the list object now has 1 reference.

Count = 2: When you call sys.getrefcount(x), the function itself creates a temporary reference to x so it can inspect it.

Count = 3: If you did y = x before calling the function, y is now a second permanent reference, and the function call makes it the third.

The Core Principle: Objects are never explicitly destroyed by you; they are collected by the Garbage Collector only when they become "unreachable" (their reference count hits zero).

3. Explaining "256 vs 257" (Implementation Details)
The documentation you read explains that for immutable types (like int), the implementation can return a reference to an existing object with the same value.

Small Integer Interning: CPython pre-allocates integers from -5 to 256 when it starts. When you say a = 256 and b = 256, they both point to the exact same pre-existing PyObject in memory. Hence, a is b is True.

The 257 Case: Since 257 is outside that range, CPython creates a new object for a and a new object for b. They have the same value but different identities (memory addresses). Thus, a is b is False.

Mutable Guarantee: For lists, even if they are empty, Python guarantees they will be unique objects. c = []; d = [] will always have different IDs because you must be able to mutate one without affecting the other.
"""