# Создаем функцию для просмотра текущих заметок
def display_notes(note):

    # Главный цикд программы
    while True:

        # Проверка на наличие заметок
        if len(note) == 0:
            print("У вас нет сохраненных заметок.")
            break

        # Если заметки найдены выводит информацию по заметкам
        else:
            id_ = 0
            print(f"\nСписок заметок:")
            for items in note:
                id_ += 1
                print("_" * 14)
                print(f"\nЗметка №{id_}.")
                print(f"Имя пользователя: {items['username']}")
                print(f"Заголовок: {items['title']}")
                print(f"Описание: {items['descriptions']}")
                print(f"Статус: {items['status']}")
                print(f"Дата создания: {items['created_date']}")
                print(f"Дата дедлайна: {items['issue_date']}")
        break
    return note

if __name__ == '__main__':
    # Заметка 1 (для тестирования)
    note_1 = [
        {'username': "Арам", 'title': "Тренировка", 'descriptions': "Расписание", 'status': "новая",
         'created_date': "24-01-2025", 'issue_date': "30-01-2025"},
        {'username': "Андрей", 'title': "Рецепт", 'descriptions': "Список покупок", 'status': "в процессе",
         'created_date': "26-01-2025", 'issue_date': "05-02-2025"},
        {'username': "Соня", 'title': "Сериалы", 'descriptions': "Просмотр на выходных", 'status': "завершена",
         'created_date': "28-01-2025", 'issue_date': "10-02-2025"}
    ]
    # Заметка 2 (для тестирования)
    note_2 = [
        {'username': "Иван", 'title': "Тренировка", 'descriptions': "Расписание", 'status': "новая",
         'created_date': "24-01-2025", 'issue_date': "30-01-2025"},
        {'username': "Артём", 'title': "Рецепт", 'descriptions': "Список покупок", 'status': "в процессе",
         'created_date': "26-01-2025", 'issue_date': "05-02-2025"},
        {'username': "Кристина", 'title': "Сериалы", 'descriptions': "Просмотр на выходных", 'status': "завершена",
         'created_date': "28-01-2025", 'issue_date': "10-02-2025"}
    ]
    display_notes(note_2)