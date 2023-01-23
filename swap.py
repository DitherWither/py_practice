#!/usr/bin/env python3

def main():
    num_a, num_b = [int(input(f"Enter number {i + 1}: ")) for i in range(2)]

    num_a, num_b = num_b, num_a
    print(num_a, num_b)


if __name__ == '__main__':
    main()
