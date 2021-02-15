class Employee:
    def __init__(self, firstname: str, lastname: str, salary: int) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary


    @classmethod
    def from_string(self, employee_info: str):
        parsed_info = employee_info.split('-')
        return Employee(parsed_info[0], parsed_info[1], int(parsed_info[2]))


employee1 = Employee('Marry', 'Sue', 60000)
employee2 = Employee.from_string("John-Smith-55000")
print(employee2.firstname, employee2.lastname, employee2.salary)
