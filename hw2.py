# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# перший записує в список нову справу
# другий повертає всі записи
def notebook(add_task=None):
    todo_list = []

    def add_todo(todo, task=None):
        nonlocal todo_list
        todo_list.append(task)
        print("Task added:", task)

    def get_all_tasks():
        return todo_list

    return add_task, get_all_tasks
# 2) протипізувати перше завдання

def tasks() -> callable:
    list_tasks: list[str] = []

    def write_task() -> None:
        nonlocal list_tasks
        number_of_tasks: int = int(input("Enter number of tasks: "))
        for i in range(number_of_tasks):
            task: str = input("Enter any task:")

            list_tasks.append(task)

    def display_tasks() -> list[str]:
        nonlocal list_tasks
        print(list_tasks)
        return list_tasks

    return write_task, display_tasks


write_task, display_tasks = tasks()

write_task()

display_tasks()

# 4)створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій


def decor(func):
    def wrapper(count):
        count += 1
        func(count)

    return wrapper
@decor
def counting(count):
    print(count)

counting(0)
counting(1)
