import ui
from exercise import Exercise
from user_answer import UserAnswer


exercise = Exercise()
task = exercise.generate_task()
ui.print_task(task)
exercise.execute_task()
user_answer = UserAnswer(ui.get_answer())
result = exercise.check_answer(user_answer.answer)
ui.print_result(result)
