# '''
# LISTS
# A list is a collection of ordered items that can be changed (mutable).
# Lists are written inside square brackets [ ] and can hold different data types.
# You can add, remove, or modify items

# TUPLES
# A tuple is similar to a list but cannot be changed once created (immutable).
# Tuples are written inside parentheses ( ).

# LOOPS (For, While)

# fOR LOOP
# Used when you want to repeat something a specific number of times

# WHILE LOOP
# Used when you want to repeat something as long as a condition is true.
# '''
# # # a times table
# table = range(1,13)
# num = int(input('enter a number: '))
# for dav in table:
#     print(f'{num} x {dav} = {num*dav}')

# # lists
# # x = ['apple', 'banana', 'mango', 'orange']
# # print(x)

# # # tuple
# # y = ('benz', 'honda', 'starlet')
# # print(y)


# # diff btn list and tuple 
# # the brackets
# # lists are changeable while tuples are unchangeable

# # add, remove or modify a list
# x = ['apple', 'banana', 'mango', 'orange']
# print(x)
# # to add we use the .append() function
# x.append('garri')
# x.append('groundnut')
# print(x)
# # to remove an item
# # we use .pop()
# x.pop(1)
# print(x)
# x.pop(3)
# print(x)
# # another way to remove a list is var name.remove('mango')

# # example of for loop
# # note for loops are used to repeat something a specific number of times 
# for x in 'banana':
#     print(x)
# # feel free to try yours with any fruit or your name

# # for loop using lists
fruits = ['apple', 'banana', 'mango', 'orange']
for x in fruits:
    print(x)

# # i just love using x pls feel free to use anything

# # for loop using numbers
# for x in range(10):
#     print(x)

# # while loop is used to repeat something without a specific number of times
# y = 1
# while y < 5:
#     print(y)
#     y += 1
# # dont forget your comparison operators += used to increment


# email = input('enter your email: ')
# if email == '123':
#     print(f'your email {email} is valid')
# else:
#     print('invalid email')

for x in range(6,9):
    print(x)