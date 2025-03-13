import re

# Считываем строки из файла и ищем даты
try:
    with open('dates.txt', 'r') as f:
        text = f.read()
        # Ищем даты в формате DD.MM.YYYY
        dates = re.findall(r'\b\d{2}\.\d{2}\.\d{4}\b', text)
        for date in dates:
            print(date)
except FileNotFoundError:
    print("Файл не найден!")
