# Создаем словарь где ключем будет название заметки а значением статус
statuses = {'Заметка': "в процессе"}

# Главный цикл программы
while True:

# Текущий статус заметки
    print(f"Текущий статус заметки: ", statuses['Заметка'])
    print("Выберите новый статус заметки: ",
                                    "1. выполнена", "2. в процессе", "3. отложено", sep = '\n')
# Выбор пользователя
    status = input("Ваш выбор: ")

# Цикл ввода пользователя
    if status == "1" or status == "выполнена":
        statuses['Заметка'] = "выполнена"
        print("Обновленный статус заметки:", statuses['Заметка'])
    elif status == "2" or status == "в процессе":
        statuses['Заметка'] = "в процессе"
        print("Обновленный статус заметки:", statuses['Заметка'])
    elif status == "3" or status == "отложено":
        statuses['Заметка'] = "отложено"
        print("Обновленный статус заметки:", statuses['Заметка'])
    else:
        print("Вы ввели некорректный ответ!!! ")
        continue

# Запрос пользователя на подтверждение
    choise = input("Подтверждаете изменение статуса заметки? ('да' или 'нет'): ")
    if choise == "да":
        print("Статус заметки успешно изменен на:", statuses['Заметка'])
        break
    else:
        continue

