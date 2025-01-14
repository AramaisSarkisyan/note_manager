# Создаем пустой список для хранения заголовков
titles = []

# Главный цикл программы
while True:
    title = input("Введите заголовок заметки (или нажмите Enter "
                  "для завершения): ").strip()
    if title == "":
        break
    titles.append(title)

# Удаляем из списка повторяющиеся заметки
titles = list(set(titles))

# Выводим введенные данные на экран
print("\nЗаголовки заметки:")
for key in titles:
    print(f"- {key.capitalize()}")