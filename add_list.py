from add_input import (
    username, content, status, created_date, issue_date)

username, content, status, created_date, issue_date

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

print("\nВы ввели следующие данные:")
print("Имя пользователя: ", username)
print("Заголовок заметки:", titles)
print("Описание заметки: ", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата создания заметки:", issue_date)