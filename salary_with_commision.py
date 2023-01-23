#!/usr/bin/env python3

def main():
    salary = int(input("Enter basic salary: "))

    commission = (salary / 100) * 20
    total_salary = salary + commission

    print(f"Salary to pay is {total_salary}")


if __name__ == '__main__':
    main()
