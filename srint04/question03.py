class Employee:
    def __init__(self, fullname: str, **kwargs) -> None:
        self.name, self.lastname = fullname.split()[0], fullname.split()[1]

        for key in kwargs:
            setattr(self, key, kwargs[key])