import random


def check_attendance():
    """
       This function checks whether Employee is present or absent
    :return: None
    """
    employee_status = random.randint(0, 1)
    if employee_status == 0:
        print("Employee is Present")
    else:
        print("Employee is Absent")


if __name__ =='__main__':
    check_attendance()