#!/usr/bin/env python3

def main():
    a = int(input("First number: "))
    b = int(input("Second number: "))

    diff = a - b
    if diff < 0:
        print("Difference Must be positive")
    else:
        print(f"Difference is {diff}")


if __name__ == '__main__':
    main()
