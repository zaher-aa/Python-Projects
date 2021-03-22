class Employee:
    def __init__(self, ID, name, num_of_children, dollar_salary):
        self.__ID = ID
        self.__name = name
        self.__num_of_children = num_of_children
        self.__dollar_salary = dollar_salary
        self.__shekel_salary = 0
        self.__geven_allowance = 0
        self.__income_tax = 0
        self.__emp_net_pay = 0

    # @property used to make it possiable to call a method without () after its name,
    #  and it is used when a method has no parameters
    @property
    def get_name(self):
        return self.__name

    @property
    def shekel_salary(self):
        self.__shekel_salary = self.__dollar_salary * 3.5
        return self.__shekel_salary

    @property
    def allowances(self):
        if self.__num_of_children == 1 or self.__num_of_children == 2 or self.__num_of_children == 3:
            self.__geven_allowance = self.__num_of_children * 50
        elif self.__num_of_children == 4 or self.__num_of_children == 5:
            self.__geven_allowance = self.__num_of_children * 30
        else:
            self.__geven_allowance = 0
        return self.__geven_allowance

    @property
    def tax(self):
        self.__income_tax = self.shekel_salary * 0.05
        return self.__income_tax

    @property
    def net_pay(self):
        self.__emp_net_pay = self.shekel_salary + self.allowances - self.tax
        return self.__emp_net_pay


employees = [
    Employee(1, "Ali", 4, 998),
    Employee(2, "Ahmed", 5, 524.6),
    Employee(4, "Zaher", 2, 9536.845),
    Employee(9, "Osama", 3, 824),
    Employee(7, "Othman", 6, 500),
    Employee(10, "Omar", 10, 2102),
    Employee(5, "Zain",  3, 100),
    Employee(3, "Zoher", 4, 1005.5),
    Employee(6, "Khalifa", 1, 19.5),
    Employee(10, "Ramy", 3, 102)
]

employees_dict = {
    employee.get_name: employee.shekel_salary for employee in employees}
for employee in employees:
    print(
        f"Net Pay for ({employee.get_name}) is: {employee.net_pay:0.2f} Shekels.")

max_person = max(employees_dict.items(),
                 key=lambda
                 depend_on: depend_on[1])
min_person = min(employees_dict.items(),
                 key=lambda
                 depend_on: depend_on[1])
print(
    f"\nMaximum Salary: {max_person} Shekesl.")
print(f"Minimum Salary: {min_person} Shekels.")
for sal in range(len(employees)):
    total = sum(employees_dict.values())
print(f"Salaries Average: {total / len(employees)} Shekels.")
