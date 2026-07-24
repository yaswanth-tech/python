'''
input formatting
----------------

int --  int(input())
---


num = int(input('eneter a num: '))
print(num + 9)
print(type(num))

#string   --   input()

we = input('enter: ')
print(type(we))

#list

nums = list(map(int,input('Enter nums: ').split()))
print(nums)

#string

nums = input('Enter nums: ').split()
print(nums)

#tuple

nums = tuple(map(int,input('Enter nums: ').split()))
print(nums)

nums = eval(input('Enter: '))
print(type(nums))

word = 'python'
reverse_word = word[:: -1]
print(reverse_word)

nums = input("Enter: ")
nums_2 = nums[::-1]
print(nums_2)

nums = eval(input("Enter: "))
print(nums[::-1])
'''

time = input("Enter 24H Clock: ")

parts = time.split(':')
hours = int(parts[0])-12
print(hours, ':', parts[1], 'pm')

00000000




