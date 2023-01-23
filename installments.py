#!/usr/bin/env python3

def main():
    loan_amount = int(input("Loan Amount: "))
    interest_rate = int(input("Interest Rate: "))

    simple_interest = loan_amount * (interest_rate / 100)
    amount_to_pay = loan_amount + simple_interest

    installment = amount_to_pay / 12

    print(f"You have to pay {installment} per month")


if __name__ == "__main__":
    main()
