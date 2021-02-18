class MyError(Exception):
    def __init__(self, data) -> None:
        self.data = data


    def __str__(self) -> str:
        return f'You input negative number: {self.data}. Try again.'
    

def check_positive(number) -> str: 
    try:
        if int(number) > 0:
            return f'You input positive number: {int(number)}'
        elif int(number) < 0:
            raise MyError(int(number))
    except MyError as message:
        return message
    except ValueError:
        return 'Error type: ValueError!'