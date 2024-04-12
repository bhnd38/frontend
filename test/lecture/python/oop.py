class Employee:
    raise_amt = 1.03

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return (self.first + "." + self.last + "@evl.com")

    def __str__(self):
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = float(self.pay * Employee.raise_amt)



class Developer(Employee):
    raise_amt = 1.04
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("=>", emp.email())

if __name__ == "__main__":

    emp1 = Employee("david", "malan", 300)
    dev2 = Developer("john", "smith", 300, "python")
    mgr1 = Manager("good", "manage", 400, [dev2])

    print(mgr1.email())
    mgr1.add_emp(emp1)
    mgr1.print_emps()
    mgr1.remove_emp(dev2)
    print("after remove-----")
    mgr1.print_emps()
    
