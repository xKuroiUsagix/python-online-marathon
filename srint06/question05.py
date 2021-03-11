import json
import pickle
from enum import Enum


class FileType(Enum):
    BYTE = 'BYTE'
    JSON = 'JSON'


class SerializeManager:
    def __init__(self, filename, file_type):
        self.filename = filename
        self.file_type = file_type


    def __enter__(self):
        return self
    

    def __exit__(self, *args):
        pass


    def serialize(self, obj):
        if self.file_type == FileType.BYTE:
            with open(self.filename, 'wb') as file:
                pickle.dump(obj, file)
        elif self.file_type == FileType.JSON:
            with open(self.filename, 'w') as file:
                json.dump(obj, file)
        else:
            raise TypeError
            

def serialize(object, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(object)