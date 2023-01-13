import random


def calculate_dailywage():
    """
       This function calculates daily wage of an Employee
    :return: None
    """
    is_present = 0
    wage_per_hour = 20
    employee_status = random.randint(0, 1)
    if employee_status == is_present:
        full_day_hour = 8
        print("Employee is Present")
    else:
        full_day_hour = 0
        print("Employee is Absent ")
    daily_wage = full_day_hour * wage_per_hour
    print("Daily Wage of employee is:", daily_wage)


if __name__ == '__main__':
    calculate_dailywage()
