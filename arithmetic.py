import ui
from exercise import Exercise
from user_answer import UserAnswer


count_tasks = 0
count_correct = 0

level = ui.ask_difficulty_level()

while count_tasks < 5:
    exercise = Exercise()
    task = exercise.generate_task(level)
    ui.print_task(task)
    exercise.execute_task(level)

    user_answer = UserAnswer(ui.get_answer())
    result = exercise.check_answer(user_answer.answer)
    ui.print_result(result)

    count_tasks += 1

    if result == 'Right!':
        count_correct += 1

ui.print_total_score(count_correct)
answer = ui.ask_save_result()

if answer in ('yes', 'YES', 'y', 'Yes'):
    name = ui.ask_user_name()
    saved_results = ui.write_user_saving_info(name, count_correct, level)
    file_name = 'results.txt'
    file = open(file_name, 'a')
    file.write(saved_results)
    file.close()
    ui.print_save_confirmation(file_name)
else:
    exit()
