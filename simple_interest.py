#!/usr/bin/env python3

def main():
    loan_amount = int(input("Loan Amount: "))
    interest_rate = int(input("Interest Rate: "))
    simple_interest = loan_amount * (interest_rate / 100)
    print(f"Interest is {simple_interest}")


if __name__ == "__main__":
    main()
