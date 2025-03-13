import re


# Проверка пароля
def is_valid_password(password):
    # Убедимся, что длина пароля не меньше 8 символов
    if len(password) < 8:
        return False
    # Проверка наличия хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        return False
    # Проверка наличия хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        return False
    # Проверка наличия хотя бы одной цифры
    if not re.search(r'[0-9]', password):
        return False
    return True


password = input("Введите пароль: ")
if is_valid_password(password):
    print("Пароль корректен")
else:
    print("Пароль некорректен")
