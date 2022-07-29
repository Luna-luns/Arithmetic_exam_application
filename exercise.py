import random


class Exercise:
    def __init__(self):
        self.task = None
        self.answer = None

    def generate_task(self, level: str) -> str:
        if level == '1':
            first_num = get_random_number_lev1()
            second_num = get_random_number_lev1()
            operation = get_random_operation()
            self.task = f'{first_num} {operation} {second_num}'

            return self.task

        if level == '2':
            number = get_random_number_lev2()
            self.task = f'{number}'

            return self.task

    def execute_task(self, level: str) -> int:
        """eval() interprets a string as code and execute it, so we get task's answer"""
        if level == '1':
            self.answer = eval(self.task)
            return self.answer
        if level == '2':
            self.answer = int(self.task) ** 2

    def is_right_answer(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def check_answer(self, user_answer: int) -> str:
        if self.is_right_answer(user_answer):
            return 'Right!'

        return 'Wrong!'


def get_random_number_lev1() -> int:
    return random.randint(2, 9)


def get_random_number_lev2() -> int:
    return random.randint(11, 29)


def get_random_operation() -> str:
    return random.choice('+-*')
