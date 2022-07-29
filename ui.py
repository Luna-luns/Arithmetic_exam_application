def ask_difficulty_level() -> str:
    while True:
        try:
            level = input('Which level do you want? Enter a number:'
                          '\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n').strip()
            if level not in ('1', '2'):
                raise ValueError

            return level
        except ValueError:
            print('Incorrect format.')


def print_task(task: str) -> None:
    print(task)


def get_answer() -> int:
    while True:
        try:
            result = int(input().strip())
            break
        except ValueError:
            print('Wrong format! Try again.')
    return result


def print_result(result: str) -> None:
    print(result)


def print_total_score(num: int) -> None:
    print(f'Your mark is {num}/5.')


def ask_save_result() -> str:
    return input('Would you like to save the result? Enter yes or no.\n').strip()


def ask_user_name() -> str:
    return input('What is your name?\n').strip()


def write_user_saving_info(name: str, num: int, level: str) -> str:
    description = None

    if level == '1':
        description = 'simple operations with numbers 2-9'
    elif level == '2':
        description = 'integral squares of 11-29'

    return f'{name}: {num}/5 in level {level} ({description}).'


def print_save_confirmation(file_name: str) -> None:
    print(f'The results are saved in "{file_name}"')
