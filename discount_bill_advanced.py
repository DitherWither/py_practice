#!/usr/bin/env python3

def main():
    discount_percentage = 20

    price = int(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    initial_bill = price * quantity

    if initial_bill > 2000:
        discount_amount = (initial_bill / 100) * discount_percentage
        bill = initial_bill - discount_amount
    else:
        bill = initial_bill

    print(bill)


if __name__ == '__main__':
    main()
