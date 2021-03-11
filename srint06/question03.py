import json
import jsonschema
import csv
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class DepartmentName(Exception):
    def __init__(self, depart_id):
        self.depart_id = depart_id


    def __str__(self):
        return f"Department with id {self.depart_id} doesn't exists"


class InvalidInstanceError(Exception):
    def __init__(self, data):
        self.data = data


    def __str__(self):
        return self.data


def validate_json(data, schema, error_message=''):
    try:
        validate(instance=data, schema=schema)
    except ValidationError:
        raise InvalidInstanceError(error_message)


def get_depart_by_id(departs, id):
    for depart in departs:
        if depart['id'] == id:
            return depart['name']


def user_with_department(csv_file, user_json, department_json):
    USER_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
        "required": ["id", "name", "department_id"]
    }
    
    DEPARTMENT_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
        },
        "required": ["id", "name"]
    }
    
    with open(user_json) as user_f,\
         open(department_json) as depart_f,\
         open(csv_file, 'w', newline='') as csv_f:

        user_data = json.load(user_f)
        depart_data = json.load(depart_f)

        for user in user_data:
            validate_json(user, USER_SCHEMA, 'Error in user schema')
        for depart in depart_data:
            validate_json(depart, DEPARTMENT_SCHEMA, 'Error in department schema')

        depart_ids = []
        for depart in depart_data:
            depart_ids.append(depart['id'])

        writer = csv.DictWriter(csv_f, fieldnames=['name', 'department'])
        writer.writeheader()
        for user in user_data:
            if user['department_id'] in depart_ids:
                writer.writerow({'name': user['name'],
                                    'department': get_depart_by_id(depart_data, user['department_id'])})
            else:
                raise DepartmentName(user['department_id'])