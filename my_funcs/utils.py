def do_operation(a, b, operation):
    result = operation(a, b)
    print(f'result: {result}')


def select_operation(choice):
    if choice == 1:
        return division
    if choice == 2:
        return multi


def division(a, b):
    return a / b


def multi(a, b):
    return a * b


def select_operation_with_lambda(choice):
    if choice == 1:
        return lambda a, b: a + b
    if choice == 2:
        return lambda a, b: a - b


# print(do_operation(100, 2, division))
# operation = select_operation(1)
# print(operation(50, 2))
# operation = select_operation(2)
# print(operation(70, 2))
# print(do_operation(7, 10, lambda a, b: a + b))
# operation = select_operation_with_lambda(1)
# print(operation(200, 60))
def outer():
    n = 1

    def inner():
        nonlocal n
        n += 1
        print(n)

    return inner


# fn = outer()
# fn()
# fn()
# fn()
def select(input_function):
    def output_function():
        print('******************')
        input_function()
        print('******************')

    return output_function()


@select
def hello():
    print('Hello, world')


def check(input_func):
    def output_func(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = 1
        input_func(name, age)

    return output_func


@check
def print_person(name, age):
    print(f'Name: {name}, age: {age}')


# print_person('Tom', -90)
def check_number(input_func):
    def output_func(*args):
        result = input_func(*args)
        if result < 0: result = 0
        return result

    return output_func


@check_number
def sum(a, b):
    return a + b


# print(sum(10, -20))
def check_division_zero(input_func):
    def output_func(*args):
        b = args[1]
        if b == 0: print('Division by Zero')
        result = input_func(*args)
        return result

    return output_func


@check_division_zero
def div(a, b):
    return a / b


def div2(a, b):
    return a // b


def compare(a, b):
    if a > b:
        print(f'{a} > {b}')
    else:
        print(f'{a} < {b}')


people = ['Tom', 'Sam', 'Bob']
for person in people:
    print(person)

i = 0
while i < len(people):
    print(people[i])
    i += 1


def sum(a, b):
    return a + b


print(sum(10, 200))
