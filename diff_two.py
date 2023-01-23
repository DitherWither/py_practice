#!/usr/bin/env python3

def main():
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(2)]
    print(nums[0] - nums[1])


if __name__ == '__main__':
    main()
