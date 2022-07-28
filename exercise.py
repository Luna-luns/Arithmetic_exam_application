import random


class Exercise:
    def __init__(self):
        self.task = None
        self.answer = None

    def generate_task(self) -> str:
        first_num = get_random_number()
        second_num = get_random_number()
        operation = get_random_operation()
        self.task = f'{first_num} {operation} {second_num}'

        return self.task

    def execute_task(self) -> int:
        """Interprets a string as code and execute it, so we get task's answer"""
        self.answer = eval(self.task)
        return self.answer

    def is_right_answer(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def check_answer(self, user_answer: int) -> str:
        if self.is_right_answer(user_answer):
            return 'Right!'

        return 'Wrong!'


def get_random_number() -> int:
    return random.randint(2, 9)


def get_random_operation() -> str:
    return random.choice('+-*')
