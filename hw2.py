# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# перший записує в список нову справу
# другий повертає всі записи
# def notebook():
#     todo_list = []
#
#     def add_todo(todo):
#         nonlocal todo_list
#         todo_list.append(task)
#         print("Task added:", task)
#
#     def get_all_tasks():
#         return todo_list
#
#     return add_task, get_all_tasks
# 2) протипізувати перше завдання
# def create_todo_list():
#     todo_list = []
#
#     def add_task(task: str) -> None:
#         nonlocal todo_list
#         todo_list.append(task)
#         print("Task added:", task)
#
#     def get_all_tasks() -> list:
#         return todo_list
#
#     return add_task, get_all_tasks
# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
# def expanded_form(number: int) -> str:
#     str_number = str(number)
#     result = []
#     for i, digit in enumerate(str_number[::-1]):
#         if int(digit) != 0:
#             result.append(digit + '0' * i)
#     return ' + '.join(result[::-1])
# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' was called {wrapper.calls} times.")
        return result
    wrapper.calls = 0
    return wrapper


@count_calls
def example_function():
    print("Executing the example function.")

