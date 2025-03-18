# 1. Связать переменную с строкой не менее 15 символов
my_string = "Привет, это строка для теста."

# 2. Извлечь первый символ
first_char = my_string[0]

# 3. Извлечь последний символ
last_char = my_string[-1]

# 4. Извлечь третий символ с начала
third_char_from_start = my_string[2]

# 5. Извлечь третий символ с конца
third_char_from_end = my_string[-3]

# 6. Измерить длину строки
string_length = len(my_string)

# 7. Перевернуть строку
reversed_string = my_string[::-1]

# 8. Извлечь первые восемь символов
first_eight_chars = my_string[:8]

# Вывод результатов
print(f"Первый символ: {first_char}")
print(f"Последний символ: {last_char}")
print(f"Третий символ с начала: {third_char_from_start}")
print(f"Третий символ с конца: {third_char_from_end}")
print(f"Длина строки: {string_length}")
print(f"Перевернутая строка: {reversed_string}")
print(f"Первые восемь символов: {first_eight_chars}")
