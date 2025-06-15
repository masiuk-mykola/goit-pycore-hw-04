from task_1.total_salary import total_salary
from task_2.get_cats_info import get_cats_info
from task_3.directory_tree import main as print_directory_tree
from task_4.bot_assistant import main as start_bot


total, average = total_salary("task_1/salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


cats_info = get_cats_info("task_2/cats_info.txt")
print(cats_info)


print_directory_tree()


start_bot()
