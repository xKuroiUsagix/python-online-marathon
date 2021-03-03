import json
import re
from uuid import uuid1
from enum import Enum


class ForbiddenException(Exception):
    pass


class PasswordValidationException(Exception):
    pass


class NonUniqueException(Exception):
    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return f'User with name {self.msg} already exists'


class Role(Enum):
    """
    Role enumerator.
    Defines roles.
    Current roles: Trainee, Mentor
    """
    Trainee = 0
    Mentor = 1


class Score(Enum):
    """
    Score enumerator.
    Defines grades from E to A
    """
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'


class Subject:
    """
    Class Subject.
    Represents the subject with:
        - id (UUID)
        - title (str)
        - score (Score)
    """
    def __init__(self, title, score: Score = None) -> None:
        self.score = score
        self.title = title
        self.id = uuid1()

    def add_score(self, score: Score):
        """
        Sets Score for subject.
        """
        self.score = score

    def __repr__(self):
        try:
            return str({self.title: self.score.value})
        except AttributeError:
            return str({self.title: self.score})


class User:
    """
    Class User.
    Represents the user with:
        - username (str)
        - password (str)
        - role (Role)
        - id (UUID)
        - subjects
    """
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role
        self.id = uuid1()
        self.subjects = []

    def add_score_for_subject(self, subject: Subject, score: Score):
        """
        Sets the score for user in concrete subject.
        """
        temp = subject
        temp.score = score
        self.subjects.append(temp)

    @classmethod
    def create_user(cls, username, password, role):
        """
        Returns the new User object with attributes:
            - username
            - password
            - role
        """
        return cls(username, cls.validate_password(password), role)

    @staticmethod
    def validate_password(password):
        """
        Checks if password is valid.
        Password must:
            - At least 6 symbols
            - At least 1 uppercase letter
            - At least 1 lowercse letter
            - At least 1 number
            - At lest 1 special character

        If password invalid raises PasswordValidationException
        Else returns password
        """
        validation_pattern = re.compile(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{6,30}$"
        )
        if not re.fullmatch(validation_pattern, password):
            raise PasswordValidationException
        else:
            return password

    def __str__(self):
        return f'{self.username} with role {self.role}: {self.subjects}'


def add_user(user, users):
    """
    Adds User to users list if User not in list already.
    Else raises NonUniqueException.
    """
    if check_if_user_present(user.username, user.password, users):
        raise NonUniqueException(user.username)
    users.append(user)


def add_subject(subject, subjects):
    """
    Adds Subject to subjects list if Subject not in list already.
    Else raises NonUniqueException.
    """
    for subject_ in subjects:
        if subject_.title == subject.title:
            raise NonUniqueException
    subjects.append(subject)


def grades_to_json(users, subjects, filename):
    """
    Serialize Grades to json.

    JSONCHEMA:
    [
        "type": "object",
        "properties": {
            "user_id": {"type": "string"},
            "subject_id": {"type": "string"},
            "score": {"type": "string"}
        }
    ]
    """
    to_json = []
    for user in users:
        for subject in user.subjects:
            dict_ = {
                'user_id': str(user.id),
                'subject_id': str(subject.id)
            }
            # There is bug when score == str. Need to fix
            if not isinstance(subject.score, str):
                dict_['score'] = subject.score.value
            else:
                dict_['score'] = subject.score
        to_json.append(dict_)

    with open(filename, 'w') as file:
        json.dump(to_json, file, indent=4)


def users_to_json(users, json_file):
    """
    Serialize Users to json.

    JSONCHEMA:
    [
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "username": {"type": "string"},
            "password": {"type": "string"},
            "role": {"type": "string"}
        }
    ]
    """
    user_list = []
    for user in users:
        user_list.append({
            # UUID
            'id': str(user.id),
            'username': user.username,
            'password': user.password,
            'role': user.role.__str__()
        })
    with open(json_file, 'w') as file:
        json.dump(user_list, file, indent=4)


def subjects_to_json(subjects, json_file):
    """
    Serialize Subjects to json.

    JSONCHEMA:
    [
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "title": {"type": "string"}
        }
    ]
    """
    to_json = []
    for subject in subjects:
        dict_ = {
            # UUID
            'id': str(subject.id),
            'title': subject.title
        }
        to_json.append(dict_)
    with open(json_file, 'w') as file:
        json.dump(to_json, file, indent=4)


def get_users_with_grades(users_json, subjects_json, grades_json):
    """
    Reads users from file if the user has grades.
    Returns a users list
    If there no such key as: 'id', 'user_id', 'username',
                             'password', 'role', 'subject_id', 'score'
    Returns an empty list.
    """
    with open(users_json) as users_file,\
         open(subjects_json) as subjects_file,\
         open(grades_json) as grades_file:
        users_data = json.load(users_file)
        subjects_data = json.load(subjects_file)
        grades_data = json.load(grades_file)

    users = []
    for user in users_data:
        new_user = 0
        for grade in grades_data:
            try:
                # Finds the user who has grade
                if user['id'] == grade['user_id'] and new_user == 0:
                    new_user = User(user['username'],
                                    user['password'],
                                    user['role'])

                # Adds all subjects for this user with grade
                if user['id'] == grade['user_id']:
                    for subject in subjects_data:
                        if subject['id'] == grade['subject_id']:
                            new_user.add_score_for_subject(
                                Subject(subject['title'], None),
                                Score(grade['score']).name
                            )
            except KeyError:
                return []
        users.append(new_user)
    return users


def get_subjects_from_json(subjects_json):
    """
    Reads subjects from json.
    Returns a subject list.
    If there no such key as 'title', returns an empty list.
    """
    with open(subjects_json) as file:
        subjects_data = json.load(file)

    subjects = []
    for subject in subjects_data:
        try:
            subjects.append(Subject(subject['title'], None))
        except KeyError:
            return []
    return subjects


def check_if_user_present(username, password, users):
    """
    Returns True | False
    Returns True if the username == user.username and password == user.password
    Else returns False
    """
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False


def get_grades_for_user(username, user: User, users):
    """
    Returns a list of subjects for user with 'username'.

    If the User Role is Mentor returns subjects anyway.
    If the User Role is Trainee, checks if the User.username == 'username'.
    Return subjects list if previous statement is True.
    Else raises ForbiddenException
    """
    if user.role == Role.Mentor:
        for user_ in users:
            if username == user_.username:
                return user_.subjects
    elif username == user.username:
        return user.subjects
    else:
        raise ForbiddenException
