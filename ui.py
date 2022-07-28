def print_task(task: str) -> None:
    print(task)


def get_answer() -> int:
    result = None
    while True:
        try:
            result = int(input().strip())
            break
        except ValueError:
            print('Incorrect format.')
    return result


def print_result(result: str) -> None:
    print(result)


def print_correct_number(num: int) -> None:
    print(f'Your mark is {num}/5.')
