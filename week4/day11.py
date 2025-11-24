'''
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the:
-try and except statement
-else keyword to define a block of code to be executed if no errors were raised:
-Raise keyword

As a Python developer you can choose to throw an exception if a condition occurs.

'''
def simple_calc():
    try:
        x = float(input('enter a number: '))
        y = float(input('enter a second number: '))
        symbol = input('choose a symbol ( +, -): ')
        if symbol == '+':
            print(x + y)
        elif symbol == '-':
            print(x - y)
        else:
            print('invalid input')
    except ZeroDivisionError:
        print('you cannot divide the number by zero')
    except ValueError:
        print('you entered an alphabet enter a number')


def word_search():
    words = ['boy', 'girl', 'man', 'dunama','barka', 'nelson']
    search = input('enter a word: '.upper()).lower()
    if search == 'boy':
        print('present')
    elif search == 'girl':
        print('present')
    elif search == 'man':
        print('present')
    elif search == 'dunama':
        print('present')
    elif search == 'barka':
        print('present')
    elif search == 'girl':
        print('present')
    else:
        print('please enter a valid word')

# simple_calc()
word_search()