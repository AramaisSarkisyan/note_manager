from datetime import datetime

# Создаем словарь
note_ = {'username': "Иван",
         'title': "Тренировка",
         'content': "Расписание",
         'status': 'в работе',
         'created_date': '24-01-2025',
         'issue_date': '30-01-2025'}

# Создаем функцию для изменения заметок
def update_note(note_):
    print(f"Текущие данные заметки.")
    print(f"\nИмя пользователя: {note_['username']}")
    print(f"Заголовок: {note_['title']}")
    print(f"Описание: {note_['content']}")
    print(f"Статус: {note_['status']}")
    print(f"Дата создания: {note_['created_date']}")
    print(f"Дата дедлайна: {note_['issue_date']}")

    # Предлагаем пользователю варианты для изменения
    update = input("\nКакие данные вы ходитет обновить? "
                   "(имя пользователя, заголовок, описание, статус, дату дедлайна): ").lower().strip()

    # цикл проверки введенных данных
    while True:
        while update not in ('имя пользователя', 'заголовок', 'описание',
                             'статус', 'дату дедлайна'):
            print("Введите правильные данные "
                  "(имя пользователя, заголовок, описание, статус, дату дедлайна)")
            update = input("\nКакие данные вы ходитет обновить? ").strip().lower()
        break

    # Цикл для изменения выбранных значений
    while True:
        if update == 'имя пользователя':
            new_username = input("Введите новое имя пользователя: ").strip()
            note_['username'] = new_username
            break
        elif update == 'заголовок':
            new_title = input("Введите новый заголовок: ").strip()
            note_['title'] = new_title
            break
        elif update == 'описание':
            new_content = input("Введите новое описание: ")
            note_['title'] = new_content
            break
        elif update == 'статус':
            while True:
                print(f"\nТекущий статус заметки: ", note_['status'])
                print("\nВыберите новый статус заметки: ",
                      "1. новая", "2. в процессе", "3. завершена", sep='\n')
                new_status = input("Ваш выбор: ").strip().lower()

                if new_status == "1" or new_status == "новая":
                    note_['status'] = "новая"
                    break
                elif new_status == "2" or new_status == "в процессе":
                    note_['status'] = "в процессе"
                    break
                elif new_status == "3" or new_status == "завершена":
                    note_['status'] = "завершена"
                    break

                while new_status not in ('1', 'новая', '2', 'в процессе', '3', 'завершена'):
                    print("\nДанные введены неверно")
                    print("\nВыберите новый статус заметки: ",
                          "1. выполнена", "2. в процессе", "3. завершена", sep='\n')
                    new_status = input("Ваш выбор: ").strip().lower()
        elif update == 'дату дедлайна':
            new_issue_date = input("Введите новую дату дедлайна в формате (день-месяц-год): ").strip()
            if not new_issue_date:
                break
            try:
                new_issue_date = datetime.strptime(new_issue_date, '%d-%m-%Y').date().strftime('%d-%m-%Y')

            except ValueError:
                print("Неправильный формат!")
                continue

            note_['issue_date'] = new_issue_date

        break

    # Выводит измененные данные
    print(f"Измененные данные.")
    print(f"\nИмя пользователя: {note_['username']}")
    print(f"Заголовок: {note_['title']}")
    print(f"Описание: {note_['content']}")
    print(f"Статус: {note_['status']}")
    print(f"Дата создания: {note_['created_date']}")
    print(f"Дата дедлайна: {note_['issue_date']}")

    # Возвращаем измененный словарь
    return note_


if __name__ == '__main__':
    note_ = update_note(note_)

