import pandas as pd
# Создаем пустую таблицу с нужными столбцами
address_book = pd.DataFrame(columns=["Full_Name", "Address", "Phone", "Birth_Date"])
while True:
    print("--- Адресная книга ---")
    print("1 - Просмотреть все записи")
    print("2 - Добавить запись")
    print("3 - Изменить запись")
    print("4 - Удалить запись")
    print("5 - Выйти")
    choice = input("Выберите действие (1-5): ")
    if choice == "1":
        if len(address_book) == 0:
            print("Адресная книга пуста")
        else:
            print(address_book)  # Выводим всю таблицу в консоль
    elif choice == "2":
        name = input("Введите ФИО: ")
        address = input("Введите адрес: ")
        phone = input("Введите телефон: ")
        birth_date = input("Введите дату рождения: ")
        new_row = pd.DataFrame([[name, address, phone, birth_date]], columns=address_book.columns)
        address_book = pd.concat([address_book, new_row], ignore_index=True)  # Объединяем таблицы и обновляем индексы
        print("Запись добавлена")
    elif choice == "3":
        if len(address_book) == 0:
            print("Адресная книга пуста")
        else:
            print(address_book)
            r = int(input("Введите номер записи для изменения: "))
            if r in address_book.index:  # Проверяем, существует ли строка с таким индексом
                print("Если поле менять не надо - оставьте его пустым")
                for column in address_book.columns:  # Поочередно перебираем все колонки таблицы
                    new_value = input(f"Новое значение для поля {column}: ")
                    if new_value != "":
                        address_book.loc[r, column] = new_value  # Перезаписываем только измененное поле
                print("Запись изменена")
            else:
                print("Такой записи нет")
    elif choice == "4":
        if len(address_book) == 0:
            print("Адресная книга пуста")
        else:
            print(address_book)
            r = int(input("Введите номер записи для удаления: "))
            if r in address_book.index:
                address_book = address_book.drop(r)  # Удаляем строку из датафрейма
                address_book = address_book.reset_index(drop=True)  # Сбрасываем индексы, чтобы они шли по порядку
                print("Запись удалена")
            else:
                print("Такой записи нет")
    elif choice == "5":
        print("Выходим из программы...")
        break  # Прерываем бесконечный цикл для выхода
    else:
        print("Неверный выбор. Попробуйте снова.")