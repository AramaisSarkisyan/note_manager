from datetime import datetime

# Определяем текущую дату
current_date = datetime.now().date().strftime("%d-%m-%Y")

# Создаем список
notes_list = []

# Приветствие
print('Добро пожаловать в менеджер заметок!')

# Главный цикл программы
while True:

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
        description = input("Введите описание заметки: ")
        while not description:
            print("Описание не может быть пустым!")
            description = input("Введите описание заметки: ")
        break

    # Запрашиваем статус
    while True:
        status = input("Введите статус заметки (новая, в процессе, выполнена): ").strip().lower()
        while status not in ("новая", "в процессе", "выполнена"):
            print("Ответ неверный повторите ввод!")
            status = input("Введите статус заметки (новая, в процессе, выполнена): ").strip().lower()
        break

    # Дата создания заметки устанавливает автоматически текущую дату
    created_date = current_date

    # Запрашиваем дату дедлайна
    while True:
        deadline_day = input("Введите дату дедлайна в формате (день-месяц-год): ")
        try:
            datetime.strptime(deadline_day, "%d-%m-%Y")

        except ValueError:
            print("Ошибка вы ввели неверные данные!!!\n"
                  "Пример ввода (05-01-2025)")
            continue
        break

    # Добавление заметки в словарь
    note = {
        'id': len(notes_list) + 1,
        'username': username,
        'title': title,
        'description': description,
        'status': status,
        'created_date': created_date,
        'deadline_day': deadline_day,
    }

    # Добавление заметки в список
    notes_list.append(note)

    # Запрос на добавление новой заметки
    answer = input("Хотите добавить еще одну заметку? (да или нет): ").strip().lower()
    while answer not in ("да", "нет"):
        print("Ответ неверный повторите ввод!")
        answer = input("Хотите добавить еще одну заметку? (да или нет): ").strip().lower()
        if answer == "нет":
            break
    if answer == "да":
        continue
    break

# Выводим полученные данные
print("\nСписок заметок:")
for note in notes_list:
    print(f"\n{note['id']}. Имя пользователя: {note['username']}")
    print(f"   Заголовок: {note['title']}")
    print(f"   Описание: {note['description']}")
    print(f"   Статус: {note['status']}")
    print(f"   Дата создания: {note['created_date']}")
    print(f"   Дедлайн: {note['deadline_day']}")