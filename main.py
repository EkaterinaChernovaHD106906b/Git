import time

import message


print(message.hello)
message.print_message('hello work')


def main():
    message.print_message('hello work')


if __name__ == '__main__':
    main()


def operation(a, b, code):
    match code:
        case '+':
            print(a + b)
        case '-':
            print(a - b)
        case '*':
            print(a * b)
        case '/':
            print(a / b)


operation(1.94, -30, '+')


def div(a, b):
    return a / b


def div2(a, b):
    return a // b


print(div(10, 3))
print(div2(10, 3))





