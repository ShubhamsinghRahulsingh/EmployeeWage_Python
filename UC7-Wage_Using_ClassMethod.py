import random


class Employee:
    # Class Variables
    full_time_hour = 8
    part_time_hour = 4
    wage_per_hour = 20
    maximum_working_days = 20
    maximum_working_hours = 100
    total_working_hour = 0

    def calculate_monthlywage(self):
        """
           This function Calculates Monthly wage of an Employee
        :return: None
        """
        is_full_time = 0
        is_part_time = 1
        days = 0
        while days < self.maximum_working_days and self.total_working_hour < self.maximum_working_hours:
            employee_status = random.randint(0, 2)
            if employee_status == is_full_time:
                self.total_working_hour += self.full_time_hour
                print("Employee is Present for Full time")
            elif employee_status == is_part_time:
                self.total_working_hour += self.part_time_hour
                print("Employee is Present for Part time")
            else:
                self.total_working_hour += 0
                print("Employee is Absent")
            days += 1
        monthly_wage = self.total_working_hour * self.wage_per_hour
        print("Monthly Wage of an Employee is:", monthly_wage)
        print("Total Hours Worked:", self.total_working_hour)
        print("Total Days Worked:", days)


if __name__ == '__main__':
    employee = Employee()
    employee.calculate_monthlywage()
