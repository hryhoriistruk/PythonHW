# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін

class Rectangle:
    __slots__ = 'side_x', 'side_y', 'area'

    def __init__(self, side_x, side_y):
        self.side_x = side_x
        self.side_y = side_y
        self.area = side_x * side_y

    def __mul__(self, other):
        return self.area * other.area

    def __add__(self, other):
        return self.area * other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return self.side_x * 2 + self.side_y * 2


rectangle1 = Rectangle(8, 5)
rectangle2 = Rectangle(5, 6)
print(len(rectangle1))


# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір ноги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):

    count = 0

    def __init__(self, name, age, size):
        super().__init__(age, name)
        self.size = size
        Cinderella.count += 1

    @classmethod
    def sum_count(cls):
        print(cls.count)


class Prince(Human):

    def __init__(self, name, age, shoes_size):
        super().__init__(name, age)
        self.shoes_size = shoes_size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella.size == self.shoes_size:
                print(cinderella)
                return cinderella
            else:
                print('Not suitable shoes')


cinderella1: [Cinderella] = [Cinderella('lisa', 20, 38),
                             Cinderella('nika', 21, 35)]
prince = Prince('john', 20, 38)
prince.find_cinderella(cinderella1)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
#                                                            - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
#                                                                                                                                                                                                                         - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
#                                                                                                                                                                                                                                                                                                                       - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, Book) or isinstance(item, Magazine):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
