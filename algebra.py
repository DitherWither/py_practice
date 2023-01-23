#!/usr/bin/env python3

def get_input(name):
    return int(input(f"Value for {name}: "))


def main():
    a = get_input('a')
    b = get_input('b')
    c = get_input('c')
    x = get_input('x')
    y = get_input('y')

    answer = a * (x ** 2) + b * x * y + c * (y ** 2)

    print(f"Answer is {answer}")


if __name__ == '__main__':
    main()
