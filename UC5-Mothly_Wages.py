import random


def calculate_monthlywage():
    """
       This function Calculates Monthly wage of an Employee
    :return: None
    """
    is_full_time = 0
    is_part_time = 1
    full_time_hour = 8
    part_time_hour = 4
    wage_per_hour = 20
    maximum_working_days = 20
    total_working_hour = 0
    days = 0
    while days < maximum_working_days:
        employee_status = random.randint(0, 2)
        if employee_status == is_full_time:
            total_working_hour += full_time_hour
            print("Employee is Present for Full time")
        elif employee_status == is_part_time:
            total_working_hour += part_time_hour
            print("Employee is Present for Part time")
        else:
            total_working_hour += 0
            print("Employee is Absent")
        days += 1
    monthly_wage = total_working_hour * wage_per_hour
    print("Monthly Wage of an Employee is:", monthly_wage)


if __name__ == '__main__':
    calculate_monthlywage()
