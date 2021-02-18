class ToSmallNumberGroupError(Exception): 
    def __init__(self) -> None:
        self.data = "We obtain error: Number of your group can't be less than 10"


    def __str__(self) -> str:
        return self.data


def check_number_group(number: int) -> str:
    try:
        if int(number) > 10:
            return f"Number of your group {int(number)} is valid"
        else:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError as msg:
        return msg
    except ValueError:
        return "You entered incorrect data. Please try again."