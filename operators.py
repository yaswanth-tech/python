'''Tokens
-->tokens are the smallest individual parts or units in the program

1.keywords
------------
num = 0
if
for
else
return
while
and
in

2.identifiers
-----------
variable
function name
class name


3.operators
----------
+ - =

4.literal
----------
int, str, tuple, list


operators
---------
1.arthimatic
------------
-,+,/,%,*,**

2.assignment
------------
=, +=, -=, *=, %=, /=

3.comparsion
-----------
==, !=, <=, >=, >, <
4.logical
-----------
and or not

5.identity
----------
is -- is will check the object not values, == checks values
is not

6.membership
----------
in
not in

7.bitwise
----------
&, |, ^, <<, >>
'''

num = 8
num_2 = 7
print(num + num_2)
print(num - num_2)
print(num * num_2)
print(num ** num_2)
print(num / num_2)
print(num % num_2)
print(num == num_2)
print(num != num_2)
print(num > num_2)
print(num < num_2)
print(num >= num_2)
print(num <= num_2)

num = 77
num_2 = 87
print(num < num_2 and num_2 < 100)
print(num > num_2 or num_2 < 100)
print(not(num < num_2 and num_2 < 100))

so = 1
how = 1
print(id(how))
print(id(how))
print(so is not how)
print(so == how)

so = [1,2,3,4,5]
print(7 in so)
print(7 not in so)

print(5 & 3)
print( 5 | 3)
print(5 >> 3)
print(5 << 3)
 







