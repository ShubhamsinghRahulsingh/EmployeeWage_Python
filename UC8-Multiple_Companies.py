import random


class Employee:
    def __init__(self, company_name, full_time_hour, part_time_hour, wage_per_hour, maximum_working_days,
                 maximum_working_hours):
        self.company_name = company_name
        self.full_time_hour = full_time_hour
        self.part_time_hour = part_time_hour
        self.wage_per_hour = wage_per_hour
        self.maximum_working_days = maximum_working_days
        self.maximum_working_hours = maximum_working_hours


    def calculate_monthlywage(self):
        """
           This function Calculates Monthly wage of an Employee
        :return: None
        """
        is_full_time = 0
        is_part_time = 1
        total_working_hour = 0
        days = 0
        while days < self.maximum_working_days and total_working_hour < self.maximum_working_hours:
            employee_status = random.randint(0, 2)
            if employee_status == is_full_time:
                total_working_hour += self.full_time_hour
            elif employee_status == is_part_time:
                total_working_hour += self.part_time_hour
            else:
                total_working_hour += 0
            days += 1
        monthly_wage = total_working_hour * self.wage_per_hour
        print(f"Monthly Wage of an Employee Working in {self.company_name} is:", monthly_wage)
        print("Total Hours Worked:", total_working_hour)
        print("Total Days Worked:", days)


if __name__ == '__main__':
    employee1 = Employee("Crimson", 8, 4, 20, 20, 100)
    employee1.calculate_monthlywage()
    print()
    employee2 = Employee("TCS", 10, 5, 25, 22, 110)
    employee2.calculate_monthlywage()
