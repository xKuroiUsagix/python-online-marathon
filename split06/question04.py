import json
from json import JSONEncoder


class StudentEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.__dict__
        return JSONEncoder.default(self, obj)


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses


    def __str__(self):
        return f'{self.full_name} ({self.avg_rank}): {self.courses}'


    @classmethod
    def from_json(cls, json_file):
        with open(json_file) as file:
            read = json.load(file)
        return cls(**read)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = [students] if not isinstance(students, list) else students


    def __str__(self):
        temp = []
        for student in self.students:
            temp.append(student.__str__())
        return f"{self.title}: {temp}"


    @staticmethod
    def serialize_to_json(list_of_groups: list, filename: str):
        with open(filename, 'w') as file:
            to_write = []
            for group in list_of_groups:
                to_write.append({
                    'title': group.title,
                    'students': group.students
                })
            
            json.dump(to_write, file, cls=StudentEncoder)

    
    @classmethod
    def create_group_from_file(cls, students_file: str):
        students_list = []
        with open(students_file) as students:
            read = json.load(students)
            read = [read] if not isinstance(read, list) else read
            for dictionary in read:
                students_list.append(Student(**dictionary))

        return cls(students_file[:students_file.index('.')], students_list)