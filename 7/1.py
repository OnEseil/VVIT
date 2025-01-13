class Employee:
    def __init__(self, id, name, *args):
        self.id = id
        self.name = name

    def get_info(self):
        return self.__dict__


class Manager(Employee):
    def __init__(self, id, name, department, *args):
        super().__init__(id, name, *args)
        self.department = department

    def manage_project(self):
        print(f"{self.name} - менеджер")


class Technician(Employee):
    def __init__(self, id, name, specialization, *args):
        super().__init__(id, name, *args)
        self.specialization = specialization

    def perform_maintenance(self):
        print(f"{self.name} выполняет техническое обслуживание")


class TechManager(Manager, Technician):
    def __init__(self, id, name, department, specialization, list, *args):
        super().__init__(id, name, department, specialization, *args)
        self.employee_list = list

    def add_employee(self, employee):
        self.employee_list.append(employee)

    def get_team_info(self):
        return [employee.get_info() for employee in self.employee_list]

emp = TechManager("Ivan", 1, "IT", "developer")

print(emp.get_info())

emp.add_employee(Employee("Danil", 5))
emp.add_employee(Manager("Max", 19, "Test"))

for i in emp.get_team_info():
    print(i.get_info())
