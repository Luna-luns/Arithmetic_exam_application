import ui
from exercise import Exercise
from user_answer import UserAnswer


count_tasks = 0
count_correct = 0

while count_tasks < 5:
    exercise = Exercise()
    task = exercise.generate_task()
    ui.print_task(task)
    exercise.execute_task()

    user_answer = UserAnswer(ui.get_answer())
    result = exercise.check_answer(user_answer.answer)
    ui.print_result(result)

    count_tasks += 1

    if result == 'Right!':
        count_correct += 1

ui.print_correct_number(count_correct)
