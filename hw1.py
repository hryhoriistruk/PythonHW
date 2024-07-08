# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# def extract_individual_digits(s):
#     digits = [char for char in s if char.isdigit()]
#     print(','.join(digits))
#
# st = 'as 23 fdfdg544'
# extract_individual_digits(st)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі


# def extract_numbers(s):
#     num = ''
#     numbers = []
#     for char in s:
#         if char.isdigit():
#             num += char
#         elif num != '':
#             numbers.append(num)
#             num = ''
#     if num != '':
#         numbers.append(num)
#     print(','.join(numbers))
#
# st = 'as 23 fdfdg544 34'
# extract_numbers(st)

# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
#
#
# result = [char.upper() for char in greeting]
#
#
# print(result)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# result = [num**2 for num in range(51) if num % 2 != 0]
#
#
# print(result)

# function
#
# - створити функцію яка виводить ліст

# def print_list(input_list):
#     for item in input_list:
#         print(item)
#
# my_list = [1, 2, 3, 4, 5]
# print_list(my_list)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# def find_max(a, b, c):
#     maximum = max(a, b, c)
#     print("The largest number is:", maximum)
#     return maximum
#
# result = find_max(10, 5, 8)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
# def min_max(*args):
#     minimum = min(args)
#     maximum = max(args)
#     print("The largest number is:", maximum)
#     return minimum
#
#
# result = min_max(10, 5, 8, 3, 12)

# - створити функцію яка повертає найбільше число з ліста

# def find_max_in_list(input_list):
#     return max(input_list)
#
#
# my_list = [10, 5, 8, 12, 3]
# result = find_max_in_list(my_list)

# - створити функцію яка повертає найменьше число з ліста

# def find_min_in_list(input_list):
#     return min(input_list)
#
# my_list = [10, 5, 8, 12, 3]
# result = find_min_in_list(my_list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
# def sum_list(input_list):
#     return sum(input_list)
#
#
# my_list = [1, 2, 3, 4, 5]
# result = sum_list(my_list)

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
# def calculate_average(input_list):
#     return sum(input_list) / len(input_list)
#
#
# my_list = [1, 2, 3, 4, 5]
# result = calculate_average(my_list)

# 1)Дан list:
# list = [22, 3,5,2,8,2,-23, 8,23,5]
#        - знайти мін число
#                     - видалити усі дублікати
#                                    - замінити кожне 4-те значення на 'X'

# my_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#
#
# min_num = min(my_list)
# print(f"Minimum number: {min_num}")
#
#
# unique_list = list(set(my_list))
# print("List without duplicates:", unique_list)
#
#
# for i in range(3, len(unique_list), 4):
#     unique_list[i] = 'X'
# print("List with every 4th value replaced with 'X':", unique_list)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

# def print_square(side_length):
#     for i in range(side_length):
#         if i == 0 or i == side_length - 1:
#             print('* ' * side_length)
#         else:
#             print('* ' + '  ' * (side_length - 2) + '*')
#
#
# side_length = 5
# print_square(side_length)

# 3) вывести табличку множення за допомогою цикла while


# def print_multiplication_table(n):
#     "
#     i = 1
#     while i <= n:
#         j = 1
#         while j <= n:
#             print(f"{i*j:>4}", end=" ")
#             j += 1
#         print()
#         i += 1
#
#
# print_multiplication_table(10)

# 4) переробити це завдання під меню


def multiplication_table_menu():
    choice = 0
    while choice != 3:
        print("1. Display multiplication table")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            i = 1
            while i <= 10:
                j = 1
                while j <= 10:
                    print(i, "*", j, "=", i*j)
                    j += 1
                i += 1
        elif choice == 2:
            print("Exiting the program...")
        else:
            print("Invalid choice, please try again.")


multiplication_table_menu()
