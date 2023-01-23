#!/usr/bin/env python3

def main():
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(2)]

    print(f"Minimum number is {min(nums)}")
    print(f"Maximum number is {max(nums)}")


if __name__ == '__main__':
    main()
