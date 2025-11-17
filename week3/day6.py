'''
Dictionaries
A dictionary is a collection which is ordered, changeable and do not allow duplicates.
Dictionaries are written with curly brackets {}, and have keys and values.

how to 
-add items 
update items (.update)
-remove items (.remove)

TASK
-Create a dictionary that stores details about a student.
-create a dictionary of subjects and their scores, then use a loop to display them.
'''
# exaple of dictionary
# my_info = {'name':'Dunama','age':35, 'school':'MAU'}

# print(type(my_info))

# # adding items 
my_info = {
    'name':'Dunama',
    'age':35, 
    'school':'MAU'
    }
my_info['state'] = 'Adamawa'
my_info['Gender'] = 'Male'
print(my_info)
# using update
my_info = {'name':'Dunama','age':35, 'school':'MAU'}
my_info.update({'Status':'Married', 'state':'Sokoto','level':'400', 'localgov.':'hong'})
# to add an item we use the update method 
print(my_info)

# # to remove an item in a dict we use the pop method (.pop)
my_info.pop('age')
print(my_info)

# TASK2
# -create a dictionary of subjects and their scores, then use a loop to display them.
# STEPS
# create a dict
# use a loop(for loop)
# for loop is used for specific or defined purpose WHILE while loop is used for an infinite or an unspecified purpose

subject_scores = {'maths':89, 'english':20, 'physics':40, 'chemistry':39, 'igbo':100}
# for subjects, scores  in subject_scores.items():
    print(f'{subjects} = {scores}')
print(subject_scores)