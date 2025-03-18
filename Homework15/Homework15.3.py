from datetime import datetime

# Запрашиваем дату у пользователя
date_format = "%Y-%m-%d"
date_str = input("Введите дату (ГГГГ-ММ-ДД): ")

# Преобразуем строку в объект datetime
input_date = datetime.strptime(date_str, date_format)

# Получаем текущую дату
current_date = datetime.now()

# Сравниваем даты
if input_date > current_date:
    print("Введенная дата — будущая.")
elif input_date < current_date:
    print("Введенная дата — прошлая.")
else:
    print("Введенная дата — сегодняшняя.")
