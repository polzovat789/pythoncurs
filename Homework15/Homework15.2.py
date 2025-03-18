from datetime import datetime

# Запрашиваем даты у пользователя
date_format = "%Y-%m-%d"
date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД): ")
date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД): ")

# Преобразуем строки в объекты datetime
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

# Вычисляем разницу между датами
delta = abs(date2 - date1)

# Выводим количество дней между датами
print(f"Количество дней между датами: {delta.days}")
