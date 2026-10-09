def calc_panel(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            func(first, second, '*')
        elif first == second:
            func(first, second, '+')
        elif first > second:
            func(first, second, '-')
        elif second > first:
            func(first, second, '%')
    return wrapper


@calc_panel
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(second - first)
    elif operation == '%':
        print(first % second)
    elif operation == '*':
        print(first * second)


first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

calc(first, second)
