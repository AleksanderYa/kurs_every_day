from django_q.tasks import async_task, result
from .todo import do

async_task(do, 'Alex')

# # get the result
# task_result = result(task_id)
#
# # result returns None if the task has not been executed yet
# # you can wait for it
# task_result = result(task_id, 200)
#
# # but in most cases you will want to use a hook:
#
# async_task('math.modf', 2.5, hook='hooks.print_result')
#
# # hooks.py
# def print_result(task):
#     print(task.result)
