'''
set
----
-set is an unordered collection
-set do not allows duplicate values inside it
-set mutable
-set represented in {}

'''

do = {1,2,3,2}
print(do)

#creating a empty set
so = set()
print(type(so))

'''
methods
--------
1. update
---------
use to add new value into set

syntax-- variable_name.update(itterable)
'''
do = {1,2,3}
do.update([6,8])
print(do)

do = {1,2,3}
do.update('python')
print(do)


'''
2. add()
--------
use to add new value into set

syntax -- variable_name.update(value)
'''
do = {1,2,3}
do.add(4)
print(do)

'''
3. remove()
-----------
used to delete the value from the set, incase if the value is not present in the set will get the KeyError

syntax -- variable_name.remove(value)


do = {1,2,3}
do.remove(4)
print(do)
'''

do = {1,2,3,4}
do.remove(4)
print(do)

'''
4. discard()
------------
used to del the value from the set, but never give any error incase value is not present inside the set

syntax -- variable_name.discard(value)
'''
do = {1,2,3}
do.discard(4)
print(do)

'''
5. pop()
--------
used to delete the value but this pop() will take 0 arguments inside it

syntax -- variable_name.pop()

'''
do = {1,2,3}
do.pop()
print(do)

'''
Operations
----------
1.union
-------
gives all sets value together but no duplicates

'''
do = {1,2,3}
so={3,4,5}
print(do|so)
print(do.union(so))

'''
2.intersection
--------------
common values in both sets
'''
do={1,2,3}
so={3,4,5}
print(do&so)
print(do.intersection(so))


#3.difference

do={1,2,3}
so={3,4,5}
print(so - do)
print(so.difference(do))


'''
Type convertion
---------------
Int:
----
String -- str()
'''
num = 7
print(type(num))
so = str(num)
print(type(so))

'''
Float:
------
Float -- float()
'''
num = 7
print(type(num))
so = float(num)
print(type(so))

'''
String
------
String -- str()
'''
nums = 7.77
print(type(nums))
all_ = int(nums)
print(type(all_))

'''
Integer
-------
Integer -- int
'''
nums = 7.77
print(type(nums))
all_ = int(nums)
print(all_)
print(type(all_))

'''
String
------

Integer -- int()
can't-
how = "i have 77 ruppees"
print(type(how))
who = int(how)
print(who)
print(type(who))
'''

how = "77"
print(type(how))
who = int(how)
print(who)
print(type(who))

#Float -- float()

how = "7.77"
print(type(how))
who = float(how)
print(who)
print(type(who))

#List -- list()

how = "5678"
print(type(how))
who = list(how)
print(who)
print(type(who))

#Tuple -- tuple()

how = "5678"
print(type(how))
who = tuple(how)
print(who)
print(type(who))

'''
list
----
string -- str()
'''
nums = [1,2,3,4]
print(type(nums))
all_n = str(nums)
print(all_n)
print(type(all_n))

#tuple -- tuple()

nums = [1,2,3,4]
print(type(nums))
all_n = tuple(nums)
print(all_n)
print(type(all_n))

'''
tuple
-----
list -- list()
'''
nums = {1,2,3,4}
print(type(nums))
all_n = list(nums)
print(all_n)
print(type(all_n))

#string -- str()

nums = {1,2,3,4}
print(type(nums))
all_n = str(nums)
print(all_n)
print(type(all_n))

#concatination(+)

num = 7
num_2 = 77
print(num + num_2)

any_ = "python is a "
we_ = "language"
print(any_ + we_)

nums = [1,2]
all_ = [3,4]
print(nums + all_)



                                                       












                                                       












                                                       












                                                       












                                                       








