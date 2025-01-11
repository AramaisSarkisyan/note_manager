# Создаем пустой список для хранения заголовков
titles = []

# Главный цикл программы
while True:
    title = input("Введите заголовок заметки (или нажмите Enter"
                  "для завершения): ")
    if title == " ":
        title
    elif title == "":
        break
    titles.append(title)

# Выводим введенные данные на экран
print("\nЗаголовки заметки:")
for key in titles:
    print(f"- {key.capitalize()}")