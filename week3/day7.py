'''
Python Functions
A function is a block of code which only runs when it is called.
A function can return data as a result.
A function helps avoiding code repetition.

Creating a Function
In Python, a function is defined using the def keyword, followed by a function name and parentheses:

Calling a Function
To call a function, write its name followed by parentheses
'''
print('hello Nelson')

def greetings():

    print('hello David')


def quotes():
    print('what ever the mind can concieve you can achieve')


def school_records():
    subject_scores = {'maths':89, 'english':20, 'physics':40, 'chemistry':39, 'igbo':100}
    for subjects, scores  in subject_scores.items():
        print(f'{subjects} = {scores}')


def grading_system():
    try:
        score = int(input("Enter your score (0 to 100): "))

        if score >= 90:
            print("Grade: A → Excellent 65")
        elif score >= 80:
            print("Grade: B → Good job ")
        elif score >= 70:
            print("Grade: C → Not bad ")
        elif score >= 60:
            print("Grade: D → Need more work. ")
        else:
            print("Grade: F → fail. ")
    except ValueError:
        print("Invalid input. Please enter a numeric score between 0 and 100.")


grading_system()
quotes()
greetings()
# school_records()
