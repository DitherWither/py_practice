#!/usr/bin/env python3

def main():
    salary = int(input("Enter basic salary: "))
    days_present = int(input("Enter number of days present: "))

    salary_per_day = salary / 30
    total_salary = salary_per_day * days_present

    print(f"Salary to pay is {total_salary}")


if __name__ == '__main__':
    main()
