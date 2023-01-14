import random


def calculate_dailywage():
    """
       This function uses match case to check whether Employee is present for full-time
       , part-time or is absent and then calculates daily wage accordingly
    :return: None
    """
    # is_full_time = 0
    # is_part_time = 1
    # is_absent = 2
    full_day_hour = 0
    wage_per_hour = 20
    employee_status = random.randint(0, 2)
    match employee_status:
        case 0:
            full_day_hour = 8
            print("Employee is Present for Full time")
        case 1:
            full_day_hour = 4
            print("Employee is Present for Part time")
        case 2:
            full_day_hour = 0
            print("Employee is Absent")
    daily_wage = full_day_hour * wage_per_hour
    print("Daily Wage of an Employee is:", daily_wage)


if __name__ == '__main__':
    calculate_dailywage()
