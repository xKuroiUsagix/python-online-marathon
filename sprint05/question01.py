class MyError(Exception):
    def __init__(self, data) -> None:
        self.data = data


    def __str__(self) -> str:
        return f'You input negative number: {self.data}. Try again.'
    

def check_positive(number) -> str: 
    try:
        if float(number) > 0:
            return f'You input positive number: {float(number)}'
        elif float(number) < 0:
            raise MyError(float(number))
    except MyError as message:
        return message
    except ValueError:
        return 'Error type: ValueError!'