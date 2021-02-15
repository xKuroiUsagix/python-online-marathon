class Employee:
    def __init__(self, firstname: str, lastname: str, salary: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary


    @staticmethod
    def from_string(employee_info: str):
        parsed_info = employee_info.split('-')
        return Employee(parsed_info[0], parsed_info[1], int(parsed_info[2]))



emp1 = Employee('abc', 'gbc', 300000)
emp2 = Employee.from_string('Jhon-Wheels-250000')
print(emp2.firstname, emp2.lastname, emp2.salary)