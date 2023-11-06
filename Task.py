class Employee:
    company = "ABC Corporation"

    def _init_(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display_employee_details(self):
        department = "HR"
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Company: {self.company}")
        print(f"Department: {department}")

employee1 = Employee(101, "John Doe", 50000)
employee2 = Employee(102, "Jane Smith", 60000)
print("Employee 1 ID:", employee1.emp_id)
print("Employee 2 Name:", employee2.emp_name)
print("Company:", Employee.company)
employee1.display_employee_details()