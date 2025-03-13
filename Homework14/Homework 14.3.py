import re

# Проверка пароля
def is_valid_password(password):
    if len(password) < 4:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

password = input("Введите пароль: ")
if is_valid_password(password):
    print("Пароль корректен")
else:
    print("Пароль некорректен")
