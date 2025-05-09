class linkedlist:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee_name):
        self.employees.append(employee_name)
        print(f"Employee {employee_name} added.")

    def remove_employee(self, employee_name):
        if employee_name in self.employees:
            self.employees.remove(employee_name)
            print(f"Employee {employee_name} removed.")
        else:
            print(f"Employee {employee_name} not found.")

    def list_employees(self):
        if self.employees:
            print("Employees:")
            for employee in self.employees:
                print(f"- {employee}")
        else:
            print("No employees.")

    def get_info(self):
        return f"Total Employees: {len(self.employees)}"


class Comp:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        self.employee_list = linkedlist()  # Create an instance of linkedlist to manage employees

    def add_employee(self, employee_name):
        self.employee_list.add_employee(employee_name)

    def remove_employee(self, employee_name):
        self.employee_list.remove_employee(employee_name)

    def list_employees(self):
        print(f"Employees in {self.name}:")
        self.employee_list.list_employees()

    def get_info(self):
        company_info = f"Company Name: {self.name}, Industry: {self.industry}"
        employee_info = self.employee_list.get_info()
        return f"{company_info}, {employee_info}"
