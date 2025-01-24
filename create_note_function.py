from datetime import datetime, timedelta


# Создание функции для создания заметок
def create_note():
    created_date = datetime.now().date().strftime("%d-%m-%Y")

    # Запрашиваем имя пользователя
    while True:
        username = input("Введите имя пользователя: ")
        while not username:
            print("Поле не может быть пустым!!!")
            username = input("Введите имя пользователя: ")
        break

    # Запрашиваем заголовок
    while True:
        title = input("Введите заголовок заметки: ")
        while not title:
            print("Поле не может быть пустым: ")
            title = input("Введите заголовок заметки: ")
        break

    # Запрашиваем описание заметки
    while True:
        content = input("Введите описание заметки: ")
        while not content:
            print("Описание не может быть пустым!")
            content = input("Введите описание заметки: ")
        break

    # Запрашиваем статус
    while True:
        status = input("Введите статус заметки (новая, в процессе, выполнена): ").strip().lower()
        while status not in ("новая", "в процессе", "выполнена"):
            print("Ответ неверный повторите ввод!")
            status = input("Введите статус заметки (новая, в процессе, выполнена): ").strip().lower()
        break

    # Дата создания заметки устанавливает автоматически текущую дату
    deadline = datetime.strptime(created_date, "%d-%m-%Y").date()

    # Запрашиваем дату дедлайна если дата не введена устанавливается по умолчанию 1 неделя
    while True:
        issue_date = input("Введите дату дедлайна в формате (день-месяц-год): ")
        while not issue_date:
            issue_date = deadline + timedelta(days=7)
            issue_date = issue_date.strftime("%d-%m-%Y")
            print("Установлена дата дедлайна по умолчанию.")
            break
        try:
            datetime.strptime(issue_date, "%d-%m-%Y")

        except ValueError:
            print("Ошибка вы ввели неверные данные!!!\n"
                  "Пример ввода (05-01-2025)")
            continue
        break

    # Добавляем полученные данные в словарь
    note_ = {
        'username': username,
        'title': title,
        'content': content,
        'status': status,
        'created_date': created_date,
        'issue_date': issue_date,
    }

    print("\nЗаметка успешно создана.")

    # Получаем готовый словарь
    return note_


if __name__ == '__main__':
    note_ = create_note()
    print(f"\nИмя пользователя: {note_['username']}")
    print(f"Заголовок: {note_['title']}")
    print(f"Описание заметки: {note_['content']}")
    print(f"Статус заметки: {note_['status']}")
    print(f"Дата создания заметки: {note_['created_date']}")
    print(f"Дата дедлайна: {note_['issue_date']}")
