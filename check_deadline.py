from datetime import datetime

# Определяем текущую дату и выводим информацию
current_date = datetime.now().date().strftime("%d-%m-%Y")
print("Текущая дата:", current_date)

# Переводим в формат datetime
ncurrent_date = datetime.strptime(current_date, "%d-%m-%Y")

# Основной цикл программы
while True:
    try:
        # Получем от пользователя информацию
        issue_date = input("Введите дату дедлайна (в формате день-месяц-год): ")

        # Переводим полученные данные в формат datetime
        issue_date = datetime.strptime(issue_date,"%d-%m-%Y")

        # Производим расчет кол-ва дней до дедлайна
        deadline_d = issue_date - ncurrent_date
        difference = deadline_d.days
        if difference < 0:
            print(f"Время дедлайна истекло {abs(difference)} дней назад.")
        elif difference == 0:
            print("!!!ВНИМАНИЕ!!!\n"
                  "Сегодня день дедлайна!!!")
        else:
            print(f"До дедлайна осталось {difference} дней.")

        break
    # Проверка на ошибки ввода
    except ValueError:
        print("Ошибка вы ввели неверные данные!!!\n"
              "Пример ввода (05-01-2025)")