class Testpaper:
    def __init__(self, subject: str, markscheme: list, pass_mark: str) -> None:
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self, test_taken='No tests taken') -> None:
        self.tests_taken = test_taken


    def take_test(self, test: Testpaper, answers: list):
        message = ''
        true_answers = len([i for i in range(len(answers)) if test.markscheme[i] == answers[i]])

        if true_answers / len(test.markscheme) >= int(test.pass_mark[:-1]) * 0.01:
            message = f'Passed! ({round(true_answers / len(test.markscheme) * 100)}%)'
        else:
            message = f'Failed! ({round(true_answers / len(test.markscheme) * 100)}%)'

        if isinstance(self.tests_taken, str):
            self.tests_taken = dict()
        self.tests_taken[test.subject] = message

