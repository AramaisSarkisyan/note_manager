# Создаем список с заметками
note_list = [
    {'username': "Иван", 'title': "Тренировка", 'descriptions': "Расписание"},
    {'username': "Артём", 'title': "Рецепт", 'descriptions': "Список покупок"},
    {'username': "Кристина", 'title': "Сериалы", 'descriptions': "Просмотр на выходных"}
]

# Выводим список с заметками
nid = 0
for items in note_list:
    nid += 1
    print(f"\n{nid}. Имя пользователя: {items['username']}")
    print(f"   Заголовок заметки: {items['title']}")
    print(f"   Описание заметки: {items['descriptions']}")
    print(f"___")

# Пользователь вводит слово для удаления заметки
test_word = input("Введите имя пользователя или заголовок для удаления заметки: ").strip().capitalize()

# Цикл программы для удаления выбранной заметки
for i in reversed(range(len(note_list))):
    if test_word == note_list[i]['username'] or test_word == note_list[i]['title']:
        print(f"\nЗаметка {note_list[i]['username']} успешно удалена")
        del note_list[i]
        break
    else:
        print("Заметка не найдена!")

# Выводим измененный список заметок на экран
print("\nИзмененный список заметок.")
nid = 0
for items in note_list:
    nid += 1
    print(f"\n{nid}. Имя пользователя: {items['username']}")
    print(f"   Заголовок заметки: {items['title']}")
    print(f"   Описание заметки: {items['descriptions']}")
    print(f"___")
