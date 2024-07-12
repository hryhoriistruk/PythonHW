# strings
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'
print(' ,'.join(el for el in st if el.isdigit()))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
st = 'as 23 fdfdg544 34'
print(''.join([el.replace(' ', ',') for el in st if el.isdigit() or el == ' ']))


# list comprehension
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'
print([el.upper() for el in greeting])


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
print([num ** 2 for num in range(51) if num % 2 != 0])

# function

# - створити функцію яка виводить ліст
def func_lst():
    return list(range(1, 11))


print(func_lst())

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def func_num(a, b, c):
    lst = [a, b, c]
    lst.sort(reverse=True)
    print(lst[0])
    return lst[0]


func_num(5, 101, 56)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def func(*args):
    lst = list(args)
    lst.sort(reverse=True)
    print(lst[0]) # 696
    return lst[-1] # 5


func(7,5,696,25,36,47,554,24,)


# - створити функцію яка повертає найбільше число з ліста
def num_max(lst):

    lst.sort(reverse=True)
    return lst[0] # 9


lst = [6, 9, 5, 3, 4]
num_max(lst)

# - створити функцію яка повертає найменьше число з ліста

def num_min(lst):

    lst.sort(reverse=False)
    return lst[0] # 3


lst = [6, 9, 5, 3, 4]
num_min(lst)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_lst(lst):

    new_lst = sum(lst)
    print(new_lst)
    return new_lst


lst = [6, 9, 5, 3, 4]
sum_lst(lst)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def sum_lst(lst):

    new_lst = sum(lst) / len(lst)
    print(new_lst)
    return new_lst


lst = [6, 9, 5, 3, 4]
sum_lst(lst)

# 1)Дан list:
list1 = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#   - знайти мін число
list1.sort(reverse=True)
print(list1[-1])

#   - видалити усі дублікати
new_list = set(list1)
print(new_list)

#   - замінити кожне 4-те значення на 'X'
for i in range(3, len(list1), 4):
    list1[i] = 'X'
print(list1)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square_func(n):

    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


square_func(6)

# 3) вывести табличку множення за допомогою цикла while
rows = 9
columns = 9
row = 1

while row <= rows:
    column = 1
    while column <= columns:
        res = row * column
        print(f"{res:3}", end=" ")
        column += 1
    print()
    row += 1

# 4) переробити це завдання під меню
while True:
    print('1  створити функцію яка виводить ліст')
    print('2  створити функцію яка повертає найбільше число з ліста')
    print('3  створити функцію яка повертає найменьше число з ліста')
    print('4  створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.')
    print('5  exit')

    entry = input('Enter your choice: ')

    if entry == '1':
        print(func_lst())
    if entry == '2':
        print(num_max(lst))
    if entry == '3':
        print(num_min(lst))
    if entry == '4':
        print(sum_lst(lst))
    if entry == '5':
        break
