# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва записувати не потрібно)
# with open('/Users/grigorii/Downloads/Telegram Desktop/emails (2).txt', 'r') as file:
#     emails = file.readlines()
#
# gmail_emails = [email.strip() for email in emails if 'gmail.com' in email]
#
# with open('gmail_emails.txt', 'w') as new_file:
#     for email in gmail_emails:
#         new_file.write(email + '\n')

# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
#                                      - всі покупки зберігаємо в файлі
# з функціоналу:
# * вивід всіх покупок
#              * має бути змога додавати покупку в книгу
#                                                  * має бути змога шукати по будь якому полю покупку
#                                                                                             * має бути змога показати найдорожчу покупку
#                                                                                                                                  * має бути можливість видаляти покупку по id
# (ну і меню на це все)

# import json
#
# class PurchaseNotebook:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.purchases = self.load_purchases()
#
#     def load_purchases(self):
#         try:
#             with open(self.file_name, 'r') as file:
#                 return json.load(file)
#         except FileNotFoundError:
#             return []
#
#     def save_purchases(self):
#         with open(self.file_name, 'w') as file:
#             json.dump(self.purchases, file, indent=4)
#
#     def add_purchase(self):
#         id = int(input("Enter purchase ID: "))
#         name = input("Enter purchase name: ")
#         price = float(input("Enter purchase price: "))
#         self.purchases.append({"id": id, "name": name, "price": price})
#         self.save_purchases()
#         print("Purchase added successfully!")
#
#     def display_all_purchases(self):
#         for purchase in self.purchases:
#             print(f"ID: {purchase['id']}, Name: {purchase['name']}, Price: {purchase['price']}")
#
#     def search_purchase(self):
#         field = input("Enter field to search (id, name, price): ")
#         value = input("Enter search value: ")
#         results = [purchase for purchase in self.purchases if str(purchase[field]) == value]
#         if results:
#             for purchase in results:
#                 print(f"ID: {purchase['id']}, Name: {purchase['name']}, Price: {purchase['price']}")
#         else:
#             print("No matching purchases found.")
#
#     def get_most_expensive_purchase(self):
#         if self.purchases:
#             most_expensive = max(self.purchases, key=lambda x: x['price'])
#             print(f"Most expensive purchase: ID: {most_expensive['id']}, Name: {most_expensive['name']}, Price: {most_expensive['price']}")
#         else:
#             print("No purchases found.")
#
#     def delete_purchase(self):
#         id = int(input("Enter purchase ID to delete: "))
#         self.purchases = [purchase for purchase in self.purchases if purchase['id'] != id]
#         self.save_purchases()
#         print("Purchase deleted successfully!")
#
# def main():
#     notebook = PurchaseNotebook("purchases.json")
#
#     while True:
#         print("\nPurchase Notebook Menu:")
#         print("1. Display all purchases")
#         print("2. Add purchase")
#         print("3. Search purchase")
#         print("4. Get most expensive purchase")
#         print("5. Delete purchase")
#         print("6. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             notebook.display_all_purchases()
#         elif choice == "2":
#             notebook.add_purchase()
#         elif choice == "3":
#             notebook.search_purchase()
#         elif choice == "4":
#             notebook.get_most_expensive_purchase()
#         elif choice == "5":
#             notebook.delete_purchase()
#         elif choice == "6":
#             break
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == "__main__":
#     main()

# *********Кому буде замало ось завдання з співбесіди
# Є ось такий список:
# data = [
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1111, "field": {}},
#         {"id": 1112, "field": {}},
#         {"id": 1113, "field": {}},
#         {"id": 1114, "field": {}},
#         {"id": 1115, "field": {}},
#     ],
#     [
#         {"id": 1110, "field": {}},
#         {"id": 1120, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1123, "field": {}},
#         {"id": 1124, "field": {}},
#         {"id": 1125, "field": {}},
#
#     ],
#     [
#         {"id": 1130, "field": {}},
#         {"id": 1131, "field": {}},
#         {"id": 1122, "field": {}},
#         {"id": 1132, "field": {}},
#         {"id": 1133, "field": {}},
#
#     ]
# ]
#
# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]

data = [
    [{"id": 1110, "field": {}}, {"id": 1111, "field": {}}, {"id": 1112, "field": {}}, {"id": 1113, "field": {}}, {"id": 1114, "field": {}}, {"id": 1115, "field": {}}],
    [{"id": 1110, "field": {}}, {"id": 1120, "field": {}}, {"id": 1122, "field": {}}, {"id": 1123, "field": {}}, {"id": 1124, "field": {}}, {"id": 1125, "field": {}}],
    [{"id": 1130, "field": {}}, {"id": 1131, "field": {}}, {"id": 1122, "field": {}}, {"id": 1132, "field": {}}, {"id": 1133, "field": {}}],
]

res = []
seen_ids = set()

while True:
    new_ids = []
    for sublist in data:
        for item in sublist:
            if item["id"] not in seen_ids:
                new_ids.append(item["id"])
                seen_ids.add(item["id"])
                break
    if not new_ids:
        break
    res.extend(new_ids)

print(res)
