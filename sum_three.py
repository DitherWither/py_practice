#!/usr/bin/env python3

def main():
    nums = [int(input(f"Enter number { i + 1 }: ")) for i in range(3)]
    print(f"The sum is {sum(nums)}")


if __name__ == "__main__":
    main()
