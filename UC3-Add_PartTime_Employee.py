import random


def calculate_dailywage():
    """
       This function checks whether Employee is present for full time
       , part time or is absent and then calculates daily wage accordingly
    :return: None
    """
    is_full_time = 0
    is_part_time = 1
    wage_per_hour = 20
    employee_status = random.randint(0, 2)
    if employee_status == is_full_time:
        full_day_hour = 8
        print("Employee is Present for Full time")
    elif employee_status == is_part_time:
        full_day_hour = 4
        print("Employee is Present for Part time")
    else:
        full_day_hour = 0
        print("Employee is Absent")
    daily_wage = full_day_hour * wage_per_hour
    print("Daily Wage of an Employee is:", daily_wage)


if __name__ == '__main__':
    calculate_dailywage()
