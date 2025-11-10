# error handling 
# we handle the  error uising try and except block
# example 1
# try:
#     temperature=float(input('enter the temperature:'))
#     if temperature == 0:
#         print(" It is freezing")
#     elif temperature >= 0 and temperature < 10:
#         print('it is cold')
#     elif temperature >=30 and temperature <40:
#         print('it is hot')
#     else:
#         print("extreme heat stay indoor")
# except ValueError:
#     print("invalid input please enter a number")

# expamle 2
# try:
#     score = int(input("Enter your score (0 to 100): "))

#     if score >= 90:
#         print("Grade: A → Excellent 65")
#     elif score >= 80:
#         print("Grade: B → Good job ")
#     elif score >= 70:
#         print("Grade: C → Not bad ")
#     elif score >= 60:
#         print("Grade: D → Need more work. ")
#     else:
#         print("Grade: F → fail. ")
# except ValueError:
#     print("Invalid input. Please enter a numeric score between 0 and 100.")

# revision on range
for i in range(2,21):
    print(i)