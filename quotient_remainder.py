#!/usr/bin/env python3

def main():
    nums = [int(input(f"Enter number {i + 1}: ")) for i in range(2)]
    quotient = nums[0] // nums[1]
    remainder = nums[0] % nums[1]

    print(f"Quotient is {quotient}")
    print(f"Remainder is {remainder}")


if __name__ == '__main__':
    main()
