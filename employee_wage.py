# Employee Wage UC1-UC8 using OOPS
import random


class Employee:
    def __init__(self, company_name,  wage_per_hour):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour

    def check_attendance(self):
        """
           This function checks whether Employee is present or absent
        :return: None
        """
        employee_status = random.randint(0, 2)
        if employee_status == 0:
            print("Employee is Present")
        else:
            print("Employee is Absent")

    def get_daily_hour(self):
        employee_status = random.randint(0, 2)
        if employee_status == 0:
            return 8
        elif employee_status == 1:
            return 4
        else:
            return 0

    def calculate_dailywage(self):
        """
           This function calculates daily wage of an Employee
        :return: Daily wage of an Employee
        """
        full_day_hour = self.get_daily_hour()
        return full_day_hour * self.wage_per_hour

    def calculate_monthly_wage(self):
        monthly_wage = 0
        for i in range(20):
            monthly_wage += self.calculate_dailywage()
        return monthly_wage


if __name__ == '__main__':
    employee1 = Employee("Crimson", 20)
    print("Welcome to the Employee Wage Problem")
    flag = True
    while flag:
        print("\nSelect From the Following\n1.Check Attendance\n2.Calculate DailyWage\n"
              "3.Calculate Monthlywage\n4.Wages For Multiple Companies\n5.Exit")
        select = int(input("Enter your choice:"))
        match select:
            case 1:
                employee1.check_attendance()
            case 2:
                daily_wage = employee1.calculate_dailywage()
                print("Daily Wage of an Employee is:", daily_wage)
            case 3:
                wage = employee1.calculate_monthly_wage()
                print("Monthly Wage of an Employee is:", wage)
            case 4:
                wage = employee1.calculate_monthly_wage()
                print(f"Monthly Wage of an Employee in {employee1.company_name} is:", wage)
                employee2 = Employee("TCS", 22)
                wage_ = employee2.calculate_monthly_wage()
                print(f"Monthly Wage of an Employee in {employee2.company_name} is:", wage_)
            case 5:
                flag = False
