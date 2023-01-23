#!/usr/bin/env python3

def main():
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(3)]
    average = sum(nums) / len(nums)
    print(f"Average is {average}")


if __name__ == '__main__':
    main()
